import pyautogui

# 함수 선언, Power Automate 활성화 및 최대화
def PowerAutomateActivate():
    try:
        pad = pyautogui.getWindowsWithTitle('Power Automate')[0]
        
        if pad.isActive == False: 
            pad.activate()
            print('Power Automate 활성화 완료')
        
        if pad.isMaximized == False:
            pad.maximize()
            print('Power Automate 최대화 완료')
        pyautogui.sleep(2)
    except:
        print('Power Automate 활성화 실패!')

#함수 호출
PowerAutomateActivate()

#내 흐름 클릭
FlowCheck = pyautogui.locateCenterOnScreen("FlowCheck.png", confidence=0.75) 
if FlowCheck:
    pyautogui.moveTo(FlowCheck) #이미지 가운데로 이동
    pyautogui.doubleClick()
    pyautogui.sleep(2)          #내 흐름 이동대기
    print("내 흐름 클릭 성공")
else:
    print("내 흐름 클릭 실패!")
    
#보건복지부 Python 선택
HealthSelect = pyautogui.locateCenterOnScreen("HealthSelect.png", confidence=0.75) 
if HealthSelect:
    pyautogui.moveTo(HealthSelect) #이미지 가운데로 이동
    pyautogui.click() 
    pyautogui.sleep(1)
    print("보건복지부 Python 선택 성공")
else:
    print("보건복지부 Python 선택 실패!")
    
#선택 흐름 시작
StartCheck = pyautogui.locateCenterOnScreen("StartCheck.png", confidence=0.75) 
if StartCheck:
    pyautogui.moveTo(StartCheck) #이미지 가운데로 이동
    pyautogui.click()
    print("보건복지부 Python 실행 성공")
else:
    print("보건복지부 Python 실행 실패!")