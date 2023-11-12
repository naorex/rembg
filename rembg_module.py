from rembg import remove
import cv2
import os

def rembg_module(input_path, output_path):
    input = cv2.imread(input_path)
    output = remove(input)
    cv2.imwrite(output_path, output)

if __name__ == '__main__':

    # 保存先のフォルダを指定
    os.makedirs(r"C:\Users\nao23\Documents\Python_Projects\rembg_311\workarea", exist_ok=True)
    folder_path = r"C:\Users\nao23\Documents\Python_Projects\rembg_311\workarea"

    # カレントディレクトリを指定先へ変更
    os.chdir(folder_path)

    # フォルダ内のファイル名の一覧を取得
    file_list = os.listdir(folder_path)

    # ファイルを一括処理する
    for i, file_name in enumerate(file_list):
        output = 'rembg_' + file_name
        rembg_module(file_name, output)
