import random

MAX_SEED = 2**32 - 1  # 4,294,967,295

class D2_MultiOutput:

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                # "seed": ("INT:seed", {}),
                # 入力タイプ
                "type": ([
                    "FLOAT",
                    "INT",
                    "STRING",
                    "SEED",
                ],),
                # プロンプト
                "parameter": (
                    "STRING",
                    {"multiline": True},
                ),
            },
            "optional": {
                "reset": ("D2RESET", {})
            }
        }

    RETURN_TYPES = ("LIST",)
    RETURN_NAMES = ("LIST",)
    FUNCTION = "output_list"
    CATEGORY = "D2"

    ######
    # def output_list(self, type, parameter, seed):
    def output_list(self, type, parameter, reset = ""):

        # 入力文字列を改行で分割
        param_options = parameter.strip().split('\n')

        # 出力リスト
        output_list = []

        # 文字列を検索して置換
        for option in param_options:
            if type == "INT" or type == "SEED":
                output_list.append(int(option))
            elif type == "FLOAT":
                output_list.append(float(option))
            else:
                output_list.append(option)

        return (output_list,)

    ######
    # def create_seed(self, seed_string):

    #     if seed_string == "-1":
    #         # "-1" の場合、新しいseedを生成
    #         return random.randint(0, MAX_SEED)
    #     else:
    #         try:
    #             # 文字列を整数に変換
    #             seed = int(seed_string)
    #             # 有効な範囲（0 から MAX_SEED）に収める
    #             return max(0, min(seed, MAX_SEED))
    #         except ValueError:
    #             # 数値に変換できない場合はエラーを発生させる
    #             raise ValueError(f"Invalid seed value: {seed_string}. Please provide a number or -1.")

