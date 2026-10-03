# SIGMA Oppo Direct Current State Snapshot R1

SCHEMA=SIGMA_OPPO_DIRECT_CURRENT_STATE_SNAPSHOT_R1

NATIVE_IDENTITY_SHA256=c8ccb7d9ba4f43e37d350c4bf66e515b70d5fc31fa9dd0329139a95f98c85222
OWNER_STATE_SHA256=e73a8bba0f631b9ab90d98a04211a2c025a777734e68ec15bb4561a38da66661
NATIVE_BINDING_SHA256=99e25dd665bffda45315c0720e58c527529cc5a0b8f35d2a4d566f04a41f85f5
STEP6_SHA256=9881a5fc5a295821be665d032a05cf73925c18220b4d613fb2d710e42133b895

LIVE_SIGMAC_PATH=/data/data/com.termux/files/home/SIGMA_R7_NEXT_R1/VKM/sigmac-vkm
LIVE_SIGMAC_SHA256=7c7fecc20fff9b339ca62c3ddcf65253df32fa703ab60ee88e015176cff672e4

LIVE_VKM_PATH=/data/data/com.termux/files/home/SIGMA_R7_NEXT_R1/VKM/sigma-vkm
LIVE_VKM_SHA256=0ad6424ccb84bfe2f44240bff8d1cf531a2fb0be88c61491ee113ba740269755

STEP6_EXPECT_SIGMAC=60a5c9028f79d4eca5d0e4859e0c681c276402ac93bbd56e750c2c05a83e2a98
STEP6_EXPECT_VM=c70bbfc53f70cafd044b61a4ad9d64f1e4ef8e6c13af8371ea8d0773df871d95

LIVE_MUTATION=NO_READ_ONLY
ADMISSION=NO
CUTOVER=NO

OPPO_DIRECT_SNAPSHOT_SHA256=0b1a65f7a236b72b589c703a77dd2fe12e7cd00c2e12949ddc4e1d81a2b66e41

## Classification

Identity/owner/native-binding evidence remains present, but the directly measured live compiler and VM hashes do not equal the toolchain hashes expected by the existing Step6 contract.

LIVE_SIGMAC_SHA256 != STEP6_EXPECT_SIGMAC
LIVE_VKM_SHA256 != STEP6_EXPECT_VM

Do not execute live Step6 cutover until this mismatch is classified from direct Oppo state.

Required next:
determine whether the expected historical toolchain still exists and is the authorized Step6 execution toolchain, or whether Step6's toolchain binding is stale and requires an explicitly verified rebind.

Do not overwrite or relax expected hashes merely to obtain PASS.
