import pyautogui
import time

pyautogui.PAUSE = 2
pyautogui.press ("win")
pyautogui.write("chrome")
pyautogui.press("enter")
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")
time.sleep(3)
pyautogui.click(x=608, y=508)
pyautogui.write("teste@teste")
pyautogui.press("tab")
pyautogui.write("teste")
pyautogui.press("tab")
pyautogui.press("enter")

time.sleep(3)

import pandas as pd
tabela = pd.read_csv("produtos.csv")

for linha in tabela.index:

    codigo = str(tabela.loc[linha, "codigo"])
    pyautogui.click(x=595, y=363)
    pyautogui.write(codigo)
    pyautogui.press("tab")

    pyautogui.write(str(tabela.loc[linha, "marca"]))
    pyautogui.press("tab")

    pyautogui.write(str(tabela.loc[linha, "tipo"]))
    pyautogui.press("tab")

    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    pyautogui.press("tab")

    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    pyautogui.press("tab")

    pyautogui.write(str(tabela.loc[linha, "custo"]))
    pyautogui.press("tab")

    obs = (str(tabela.loc[linha, "obs"]))
    if obs != "nan":
        pyautogui.write(obs)

    pyautogui.press("tab")
    pyautogui.press("enter")

    pyautogui.scroll(5000)


































