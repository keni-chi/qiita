# coding: utf-8
"""if __name__ == '__main__':について.

もしimportすると実行するようにしたければ以下のようにcalled.pyを書き変える。

＜変更前＞
if __name__ == '__main__':
    main()
＜変更後＞
main()

"""

print('client--------------------start')
import called
print('client--------------------end')

