import importlib.util, pathlib, subprocess, sys, tempfile, unittest

BASE = pathlib.Path(__file__).resolve().parents[1] / 'src'

def load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec); spec.loader.exec_module(mod); return mod

mwb = load('mwb', BASE/'host/mechanical_web_bridge.py')
opid = load('opid', BASE/'host/operation_id.py')
rb = load('rb', BASE/'host/resource_budget.py')

class MechanicsTests(unittest.TestCase):
    def test_operation_ids_are_class_bound_and_deterministic(self):
        a=opid.operation_id('FETCH',['GET','abc'])
        b=opid.operation_id('FETCH',['GET','abc'])
        c=opid.operation_id('DECODE',['GET','abc'])
        self.assertEqual(a,b); self.assertNotEqual(a,c)
        with self.assertRaises(ValueError): opid.operation_id('CHOOSE_SOURCE',['x'])

    def test_resource_budget_request_bound(self):
        with tempfile.TemporaryDirectory() as td:
            t=pathlib.Path(td); b=rb.CycleBudget(t/'budget')
            state={'request_count':rb.MAX_REQUESTS_PER_CYCLE,'total_bytes':0,'last_global_epoch':0.0,'last_domain_epoch':{}}
            (t/'budget'/'budget.state.json').write_text(__import__('json').dumps(state))
            with self.assertRaises(rb.BudgetError): b.acquire('public.example',t)
            b.release()

    def test_ip_policy(self):
        for ip in ['127.0.0.1','10.1.2.3','172.16.0.1','192.168.1.1','169.254.1.1','::1','fc00::1']:
            self.assertFalse(mwb._safe_ip(ip), ip)
        for ip in ['1.1.1.1','8.8.8.8','2606:4700:4700::1111']:
            self.assertTrue(mwb._safe_ip(ip), ip)

    def test_url_credentials_rejected_without_network(self):
        with self.assertRaises(mwb.PolicyError):
            mwb.validate_url('https://user:pass@example.invalid/x')
        with self.assertRaises(mwb.PolicyError):
            mwb.validate_url('file:///etc/passwd')
        with self.assertRaises(mwb.PolicyError):
            mwb.validate_url('http://127.0.0.1/', allow_http=True)

    def test_queue_exact_and_idempotent(self):
        with tempfile.TemporaryDirectory() as td:
            t=pathlib.Path(td)
            inputs={'raw':b'raw\x00bytes','native':b'native output\n','event':b'OWNER=SIGMA_NATIVE_VM\n','receipt':b'{}\n'}
            for k,v in inputs.items(): (t/k).write_bytes(v)
            import hashlib
            cmd=[sys.executable,str(BASE/'host/seal_queue.py'),'--queue-root',str(t/'q'),'--raw-content',str(t/'raw'),'--native-output',str(t/'native'),'--native-event',str(t/'event'),'--transport-receipt',str(t/'receipt'),'--native-input-sha256',hashlib.sha256(inputs['raw']).hexdigest(),'--native-output-mode','TEST_NATIVE_BYTES']
            a=subprocess.run(cmd,capture_output=True,text=True,check=True).stdout
            b=subprocess.run(cmd,capture_output=True,text=True,check=True).stdout
            self.assertIn('QUEUE_COMMIT=PASS',a)
            self.assertIn('QUEUE_COMMIT=IDEMPOTENT_REUSE',b)
            dirs=list((t/'q'/'sealed').iterdir()); self.assertEqual(len(dirs),1)
            item=dirs[0]
            self.assertEqual((item/'raw.content').read_bytes(),inputs['raw'])
            self.assertEqual((item/'native.output').read_bytes(),inputs['native'])
            self.assertTrue((item/'SEALED').is_file())

if __name__ == '__main__': unittest.main()
