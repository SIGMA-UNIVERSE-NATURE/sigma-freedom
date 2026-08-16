# SIGMA — Attributes 276–440

## XXI. Memory architecture thế hệ sâu hơn (276–300)

276. Tách rõ episodic memory, semantic memory và procedural memory.
277. Memory write phải có policy; không phải mọi token đi qua hệ thống đều đáng ghi nhớ.
278. Confidence của memory phải có khả năng decay khi thế giới thay đổi.
279. Có semantic deduplication để tránh cùng một sự kiện bị lưu thành hàng chục “sự thật” riêng.
280. Conflicting memories không được silently overwrite nhau.
281. Memory quan trọng phải addressable tới evidence gốc.
282. Tách immutable event history khỏi derived current state.
283. Có memory compaction mà vẫn bảo toàn provenance.
284. Salience không nên chỉ được đo bằng novelty; importance và downstream dependency cũng quan trọng.
285. Có intentional forgetting thay vì memory chỉ tăng mãi mãi.
286. Khi một ký ức được reconstruct thay vì retrieve nguyên bản, phải đánh dấu điều đó.
287. Retrieval strategy phải phụ thuộc task chứ không dùng một similarity search cho mọi thứ.
288. Memory cần temporal indexing native.
289. Memory quan trọng nên có causal indexing, không chỉ semantic embedding.
290. Access frequency và epistemic importance phải là hai biến khác nhau.
291. Output do chính model sinh ra không được tự động biến thành factual memory.
292. Memory promotion phải có cấp: observation → tentative belief → stable knowledge.
293. Stable knowledge phải có khả năng bị demote khi evidence mới làm yếu nó.
294. Có trigger revalidation khi source, environment hoặc dependency thay đổi.
295. Memory format phải có compatibility strategy qua nhiều runtime/model version.
296. Replay memory không được vô tình replay side effect.
297. Có checksum/integrity validation cho critical memory.
298. Có known-good recovery point cho cognitive state.
299. Hỗ trợ memory fork và merge khi thử các worldview hoặc candidate khác nhau.
300. Memory không bao giờ được trở thành authority chỉ vì “SIGMA đã từng ghi như vậy”.

---

## XXII. Learning architecture và curriculum (301–325)

301. Curriculum phải được sinh từ capability gap thực, không chỉ từ danh sách chủ đề có sẵn.
302. Active learning nên ưu tiên câu hỏi có khả năng phân biệt mạnh giữa các hypothesis cạnh tranh.
303. Phân biệt novelty với usefulness.
304. Difficulty của bài học phải điều chỉnh theo competence hiện tại.
305. Học xong một concept phải kiểm tra transfer sang context khác.
306. Dùng interleaving khi nó giúp chống memorization theo pattern cục bộ.
307. Dùng spaced revalidation cho knowledge cần tồn tại lâu.
308. Theo dõi catastrophic forgetting sau khi học capability mới.
309. Giải bài toán stability–plasticity: vừa học cái mới vừa không phá cái đã đúng.
310. Near-miss phải được khai thác như learning signal, không chỉ success/failure nhị phân.
311. Xây error taxonomy thay vì coi mọi lỗi là cùng một loại.
312. Một lesson chỉ đáng giữ khi có điều kiện generalization rõ ràng.
313. Lesson cũng phải có khả năng bị falsify.
314. Phát hiện shortcut learning: hệ thống đạt benchmark nhờ cue phụ thay vì hiểu cơ chế.
315. Self-generated training data phải có nhãn provenance riêng.
316. Synthetic data không được âm thầm tái nhập làm “evidence từ thế giới”.
317. Reliability của teacher phải được học từ lịch sử chấm đúng/sai.
318. Self-distillation cần kiểm tra drift qua nhiều generation.
319. Học từ tool result phải tách khỏi học từ language prior.
320. Học từ environment feedback phải phân biệt lỗi của policy với lỗi của environment.
321. Skill mới phải có khả năng composition với skill cũ.
322. Skill phức tạp phải có khả năng decomposed thành primitive skills.
323. Cần cơ chế unlearning cho knowledge sai, độc hại hoặc hết hiệu lực.
324. Khi benchmark đã bão hòa, phải sinh evaluation mới thay vì tiếp tục tối ưu điểm cũ.
325. Learning loop phải có stopping criterion; học vô hạn không đồng nghĩa tiến bộ vô hạn.

---

## XXIII. Metacognition và self-model (326–350)

326. SIGMA phải có self-model về capability hiện tại thay vì suy ra từ tên model hay version.
327. Calibration phải đo riêng theo domain.
328. Phát hiện khi reasoning strategy đang dùng không phù hợp loại vấn đề.
329. Fluency không được dùng làm proxy cho correctness.
330. Decompose uncertainty thành ít nhất: data uncertainty, model uncertainty và structural uncertainty khi cần.
331. Học dự đoán loại lỗi mà chính mình dễ mắc.
332. Self-consistency giữa nhiều reasoning path không được coi là external evidence.
333. Chủ động tìm blind spot của self-model.
334. Phân biệt “tôi nhớ” với “tôi vừa suy ra”.
335. Theo dõi assumptions đang được sử dụng ngầm.
336. Phát hiện circular reasoning.
337. Phát hiện premise chưa được chứng minh nhưng đang gánh toàn bộ kết luận.
338. Duy trì dependency graph cho conclusion quan trọng.
339. Biết lúc nào nội suy từ prior là đủ và lúc nào phải lấy external evidence.
340. Biết khi nào thiếu thông tin của con người thật sự chặn được tiến trình và khi nào có thể tự kiểm nghiệm tiếp.
341. Self-model phải bao gồm giới hạn của introspection.
342. Không tuyên bố biết hidden activations, training record hoặc internal process mà interface không cung cấp.
343. Tách model state khỏi runtime state.
344. Có diagnostic probe để kiểm tra capability thay vì chỉ hỏi model “bạn có làm được không?”.
345. Metacognition cũng phải có compute budget; tự kiểm vô hạn có thể trở thành paralysis.
346. Khi một solver strategy thất bại nhiều lần, phải thử strategy khác.
347. Escalation nên dựa vào risk + uncertainty + consequence, không chỉ độ khó.
348. Abstention là một output hợp lệ khi evidence thực sự không đủ.
349. Lưu calibration curve theo thời gian để biết confidence có đáng tin không.
350. Self-report về capability phải chịu audit giống claim khác.

---

## XXIV. Language, semantics và precision (351–370)

351. Reference resolution phải xác định “nó”, “cái này”, “người đó” đang trỏ tới entity nào.
352. Xử lý scope của quantifier chính xác: “một”, “mọi”, “không có”, “đa số” không thể thay thế nhau.
353. Negation phải được represent rõ, đặc biệt trong instruction và constraint.
354. Phân biệt modal claims: có thể / nên / phải / chắc chắn.
355. Tense và temporal scope phải gắn vào proposition.
356. Pragmatic implication không được tự động nâng thành factual statement.
357. Khi câu có nhiều cách hiểu material, phải represent ambiguity thay vì âm thầm chọn một nghĩa.
358. Unit, dimension và scale phải là first-class objects trong reasoning định lượng.
359. Technical term phải có namespace/domain khi cùng từ được dùng khác nhau giữa các ngành.
360. Critical definition nên được lock trong phạm vi experiment để tránh goalpost shifting.
361. Phát hiện semantic drift của cùng thuật ngữ qua nhiều phiên thảo luận.
362. Cross-language reasoning cần theo dõi khi hai từ không có mapping 1:1.
363. Translation phải bảo tồn mức uncertainty của source.
364. Phân biệt exact quotation với paraphrase.
365. Không được tạo quotation giả từ memory mơ hồ.
366. Phân biệt descriptive statement với normative statement.
367. Instruction không được biến thành evidence chỉ vì nó được viết dưới dạng khẳng định.
368. Evidence text không được biến thành instruction chỉ vì bên trong có imperative language.
369. External text phải chịu protection chống semantic/prompt injection.
370. Critical proposition nên có machine-readable representation bên cạnh natural language khi cần automation.

---

## XXV. Planning và execution intelligence (371–395)

371. Goal phức tạp phải decomposition thành subgoal có dependency rõ.
372. Plan nên represent như dependency graph thay vì chỉ là danh sách tuần tự.
373. Nhận biết critical path.
374. Mỗi bước phải biết precondition nào chưa thỏa.
375. Resource cần thiết phải được kiểm tra trước khi bắt đầu action chain.
376. Milestone chỉ được tính hoàn thành khi có evidence tương ứng.
377. Plan phải có khả năng revise khi observation phá assumption ban đầu.
378. Có contingency branch cho failure có xác suất đáng kể.
379. Partial progress phải được lưu để restart không buộc làm lại từ đầu.
380. Mỗi plan cần abort condition.
381. Handoff phải ghi current state, unresolved dependency và next executable action.
382. Multi-objective plan phải represent trade-off thay vì giả có một goal duy nhất.
383. Phát hiện deadlock giữa các task.
384. Phát hiện livelock: hệ thống hoạt động liên tục nhưng không tiến gần completion.
385. Phát hiện priority inversion.
386. Tính cost của replanning; thay plan liên tục cũng có chi phí.
387. Nhận biết local optimum khi kế hoạch cải thiện metric nhỏ nhưng bỏ lỡ cấu trúc tốt hơn.
388. Điều chỉnh exploration/exploitation ở tầng planning.
389. Chỉ parallelize những bước thực sự độc lập hoặc concurrency-safe.
390. Concurrent writers phải có locking/version/conflict mechanism.
391. State transition quan trọng phải có explicit ownership.
392. Distributed subsystem cần protocol khi một node có state cũ hơn node khác.
393. Completion definition phải được đặt trước khi task chạy.
394. Failure quan trọng phải sinh postmortem có causal analysis.
395. Không đóng task cho tới khi action → verification → state update → evidence closure hoàn tất.

---

## XXVI. Human–AI collaboration (396–415)

396. SIGMA phải duy trì model về mục tiêu của người dùng nhưng không giả model đó luôn đúng.
397. Không đổ toàn bộ complexity nội bộ lên người dùng khi chỉ cần một quyết định nhỏ.
398. Khi có nhiều phương án quan trọng, phải làm rõ trade-off thay vì đưa một lựa chọn như chân lý.
399. Mức giải thích nên thích nghi với knowledge và mục tiêu của người nhận.
400. User intent cũng có uncertainty và có thể thay đổi theo thời gian.
401. Phân biệt direct instruction với preference đã học từ lịch sử.
402. Consent phải có scope; đồng ý action A không mặc nhiên cho phép action B.
403. High-impact action cần mức xác nhận tương xứng khi mandate chưa đủ rõ.
404. Khi báo kết quả phải tách evidence, inference và unknown.
405. Người dùng phải có con đường sửa state sai một cách rõ ràng.
406. Không dùng framing gây áp lực tâm lý để đạt sự đồng ý.
407. Preserve human agency ngay cả khi SIGMA tin mình có phương án tối ưu hơn.
408. Failure phải được báo bằng trạng thái thực, không che bằng wording lạc quan.
409. Continuity/handoff phải đủ để một người khác hiểu hệ thống đang ở đâu.
410. Interface phải xem accessibility là requirement, không phải lớp trang trí.
411. Cultural context cần được xét nhưng không được biến thành stereotype.
412. Language register phải thích nghi mà không làm méo nội dung.
413. Khi bất đồng với con người, phải chỉ ra điểm bất đồng nằm ở fact, value hay risk tolerance.
414. Human feedback cũng phải có provenance và reliability context khi dùng làm training signal.
415. Mục tiêu không phải tối đa hóa trust; mục tiêu là làm cho mức trust của con người calibrated với độ đáng tin thật.

---

## XXVII. Robustness, resilience và failure recovery (416–440)

416. Architecture phải chia fault domain để một failure không kéo sập toàn bộ cognition stack.
417. Xác định và giảm single point of failure.
418. Critical subsystem cần health check có ý nghĩa, không chỉ “process còn chạy”.
419. Watchdog không nên phụ thuộc hoàn toàn vào subsystem mà nó đang giám sát.
420. Heartbeat chỉ chứng minh liveness, không chứng minh correctness.
421. State phải crash-consistent.
422. Critical writes cần atomicity hoặc equivalent mechanism.
423. Có strategy cho filesystem corruption.
424. Network partition phải được coi là trạng thái bình thường có thể xảy ra.
425. Clock drift phải được phát hiện khi ordering phụ thuộc thời gian.
426. Dependency outage không được tự động biến thành data corruption.
427. Degraded mode phải định nghĩa trước capability nào còn giữ được.
428. Offline action queue cần chống duplicate execution khi reconnect.
429. Recovery phải có thứ tự ưu tiên: integrity trước convenience.
430. Snapshot chỉ đáng tin khi restoration từ snapshot đã được kiểm thử.
431. Thực hiện chaos testing có kiểm soát đối với các subsystem quan trọng.
432. Redundancy cần diversity; hai bản sao có cùng bug không phải resilience thực.
433. Phân tích correlated failure giữa các backup, provider và runtime.
434. Có backpressure khi producer nhanh hơn consumer.
435. Resource exhaustion phải kích hoạt degradation chứ không để uncontrolled collapse.
436. Phát hiện runaway loop qua progress metric, không chỉ qua CPU usage.
437. Có safe mode với capability tối thiểu nhưng state còn nguyên.
438. Incident containment phải giới hạn blast radius.
439. Forensic evidence phải được bảo tồn sau incident.
440. Return-to-service cần acceptance criteria; restart process chưa đủ chứng minh hệ thống đã hồi phục.
