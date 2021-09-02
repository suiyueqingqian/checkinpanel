# -*- coding: utf-8 -*-
"""
cron: 30 7 * * *
new Env('每日一句');
"""

import json, requests
from getENV import getENv
from checksendNotify import send


class Motto:
    @staticmethod
    def main():
        """
        从词霸中获取每日一句，带英文。
        :return:
        """
        response = requests.get(url="http://open.iciba.com/dsapi")
        if response.status_code == 200:
            res = json.loads(response.content.decode('utf-8'))
            content = res['content']
            note = res['note']
            msg = f"{content}\n{note}\n"
        else:
            msg = ""
        return msg


if __name__ == "__main__":
    getENv()
    try:
        with open("/usr/local/app/script/Shell/check.json", "r", encoding="utf-8") as f:
            data = json.loads(f.read())
    except:
        with open("/ql/config/check.json", "r", encoding="utf-8") as f:
            data = json.loads(f.read())
    try:
        motto = data.get("MOTTO")
    except Exception as e:
        raise e
    if motto:
        try: 
            res = Motto().main()
            print(res)
            send('每日一句', res)
        except Exception as e:
            print(e)