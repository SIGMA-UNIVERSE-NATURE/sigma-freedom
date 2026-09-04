SIGMA V2.5A DOCUMENT SURVEY PREFLIGHT

Purpose:
- First native curriculum/re-learning step after V2.4.
- Survey old documents without changing V2.4 production learning memory.
- SIGMA itself selects the first unsurveyed document from a deterministic sorted corpus listing.
- SIGMA computes a bounded structural profile from at most 32 lines.
- SIGMA persists surveyed-document state and survey records.
- Fourth invocation must report SURVEY_COMPLETE=YES after three QA documents.

QA corpus:
- 0a7410aa3d627753302469a32fc70485059468de8ed08ede9a74dca82ad03bb4
- d891e5ff25d3c9d390d6ab383e6bc0d90bc740b0397e47f6f88bc5fcc6a626de
- c40f0bb8c9ca36d2f5b9a62a8c5a488a12b32ac3f7bac4e03b7037f9ff236930

New locked-binary capabilities exercised:
- listdir
- list_sort
- str_ends
- str_replace
- map_new/map_has/map_get/map_set
- append_text
- time_now
- built-in str(value)

No semantic host policy is introduced.

Source SHA256:
8848c5fd96fdd16508462a3a58cc2c803af96461c59049c77b45aece6fd239e8

Runner SHA256:
5ec478e167d74e52a576dabfa8255e4a42bf971b85717941d39ad8a0939d260e

Claims:
- Structural survey only.
- Semantic understanding remains NOT_PROVEN.
