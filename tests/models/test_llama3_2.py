from model_test import ModelTest


class TestLlama3_2(ModelTest):
    NATIVE_MODEL_ID = "/monster/data/model/Llama-3.2-1B-Instruct" # "meta-llama/Llama-3.2-1B-Instruct"
    NATIVE_ARC_CHALLENGE_ACC = 0.3567
    NATIVE_ARC_CHALLENGE_ACC_NORM = 0.3805
    QUANT_ARC_MAX_DELTA_FLOOR_PERCENT = 0.36
    APPLY_CHAT_TEMPLATE = True
    TRUST_REMOTE_CODE = True

    def test_llama3_2(self):
        self.quant_lm_eval()
