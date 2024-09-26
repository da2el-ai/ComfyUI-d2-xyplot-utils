import re

class D2_RegexSwitcher:

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                # 検索対象テキスト
                "text": (
                    "STRING",
                    {"forceInput": True, "multiline": True},
                ),
                # 正規表現、出力テキストのペア
                "regex_and_output": (
                    "STRING",
                    {"multiline": True},
                ),
            },
        }

    RETURN_TYPES = ("STRING","INT",)
    RETURN_NAMES = ("text","index",)
    FUNCTION = "regex_switch"
    CATEGORY = "D2"

    ######
    def regex_switch(self, text, regex_and_output):
        # regex_and_output を -- で分割し、ペアにする
        pairs = regex_and_output.split('--')

        # ペアをリストに整理する
        regex_output_list = []
        default_output = None
        for i in range(0, len(pairs), 2):
            if i + 1 < len(pairs):
                regex = pairs[i].strip()
                output = pairs[i+1].strip()
                if regex:
                    regex_output_list.append({
                        'regex': regex,
                        'output': output
                    })
                else:
                    default_output = output

        # 各正規表現をチェックし、マッチしたら対応する出力を返す
        for index, item in enumerate(regex_output_list):
            if re.search(item['regex'], text, re.IGNORECASE):
                # return (item['output'],)
                return {"ui": {"text": text}, "result": (item['output'],index,)}

        # マッチしなかった場合はデフォルト出力を返す
        return {"ui": {"text": text}, "result": (default_output, -1)}
