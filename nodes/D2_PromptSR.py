#
# A text replacement function that outputs input as a list, designed for use with qq-nodes-comfyui.
#

class D2_PromptSR:

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                # プロンプト
                "prompt": (
                    "STRING",
                    {"multiline": True},
                ),
                # 検索ワード
                "search_txt": (
                    "STRING",
                    {"multiline": False},
                ),
                # 置換文字列
                "replace": (
                    "STRING",
                    {"multiline": True},
                ),
            },
        }

    RETURN_TYPES = ("LIST",)
    RETURN_NAMES = ("LIST",)
    FUNCTION = "replace_text"
    CATEGORY = "D2"

    def replace_text(self, prompt, search_txt, replace):
        # 置換文字列を改行で分割
        replace_options = replace.strip().split('\n')

        # 出力リスト
        output_list = [prompt]

        # 文字列を検索して置換
        for option in replace_options:
            new_prompt = prompt.replace(search_txt, option)
            output_list.append(new_prompt)

        return (output_list,)
