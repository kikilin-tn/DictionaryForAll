import os
import time

filename = input('請輸入想要使用的小字典檔名:(例如:Dictionary for enews.csv)\n')

if os.path.isfile(filename):
    print('歡迎使用萬用小字典')
    with open(filename, 'r', encoding = 'utf-8') as f:
        result = {}
        for line in f.readlines():
            line = line.strip()
            if not len(line):
                continue
            result[line.split(',')[0]] = line.split(',')[1]
else:
   print(filename + '檔案不在資料夾中，請放置於相同資料夾內')

KC_dic = result
print('************************')
print('請輸入日文字。或按q退出')
print('************************')

while True:
  JP_word = input()
  if JP_word == 'q':
    print('請跳出檢視外部檔案' + filename)
    time.sleep(3)
    break

  if JP_word in KC_dic:
    #for key,value in KC_dic.items():
    print('************************')
    print('查詢結果: 對應的中文字義為[' + KC_dic[JP_word] + ']')
    print('************************')
    print('繼續使用時，請輸入日文字。或按q退出')
  else:
    print(JP_word+' 這個字還沒對應的中文，請輸入適當的中文')
    CH_word = input()
    KC_dic[JP_word] = CH_word
    KC_dic.update({JP_word:CH_word})
    print('中文已被更新')
    print('繼續使用時，請輸入日文。或按q退出')

with open(filename,'w', encoding='utf-8') as fout:
    for k, v in KC_dic.items():
        dic = k +','+ v + '\n'
            #print(dic)
        fout.write(dic)
    print(fout)
