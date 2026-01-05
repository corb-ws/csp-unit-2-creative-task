from cmu_graphics import *
#Counters
counter1=Label(0,47,20,visible=False)
counter2=Label(0,98,20,visible=False)
counter3=Label(0,149,20,visible=False)
counter4=Label(0,200,20,visible=False)
counter5=Label(0,251,20,visible=False)
counter6=Label(0,302,20,visible=False)
counter7=Label(0,353,20,visible=False)
holder1=Rect(0,75,400,350,fill='blue',visible=False)
holder2=Rect(11,86,378,350,fill='darkBlue',visible=False)
def addToRed(piece):
    if(piece.fill=='red'):
        redList.add(
            piece)
def addToYellow(piece):
    if(piece.fill=='yellow'):
        yellowList.add(piece)
#Pieces
#Column 1
piece1=Circle(47,374,25,fill='white')
piece2=Circle(47,323,25,fill='white')
piece3=Circle(47,272,25,fill='white')
piece4=Circle(47,221,25,fill='white')
piece5=Circle(47,170,25,fill='white')
piece6=Circle(47,119,25,fill='white')
#Column 2
piece7=Circle(98,374,25,fill='white')
piece8=Circle(98,323,25,fill='white')
piece9=Circle(98,272,25,fill='white')
piece10=Circle(98,221,25,fill='white')
piece11=Circle(98,170,25,fill='white')
piece12=Circle(98,119,25,fill='white')
#Column 3
piece13=Circle(149,374,25,fill='white')
piece14=Circle(149,323,25,fill='white')
piece15=Circle(149,272,25,fill='white')
piece16=Circle(149,221,25,fill='white')
piece17=Circle(149,170,25,fill='white')
piece18=Circle(149,119,25,fill='white')
#Column 4
piece19=Circle(200,374,25,fill='white')
piece20=Circle(200,323,25,fill='white')
piece21=Circle(200,272,25,fill='white')
piece22=Circle(200,221,25,fill='white')
piece23=Circle(200,170,25,fill='white')
piece24=Circle(200,119,25,fill='white')
#Column 5
piece25=Circle(251,374,25,fill='white')
piece26=Circle(251,323,25,fill='white')
piece27=Circle(251,272,25,fill='white')
piece28=Circle(251,221,25,fill='white')
piece29=Circle(251,170,25,fill='white')
piece30=Circle(251,119,25,fill='white')
#Column 6
piece31=Circle(302,374,25,fill='white')
piece32=Circle(302,323,25,fill='white')
piece33=Circle(302,272,25,fill='white')
piece34=Circle(302,221,25,fill='white')
piece35=Circle(302,170,25,fill='white')
piece36=Circle(302,119,25,fill='white')
#Column 7
piece37=Circle(353,374,25,fill='white')
piece38=Circle(353,323,25,fill='white')
piece39=Circle(353,272,25,fill='white')
piece40=Circle(353,221,25,fill='white')
piece41=Circle(353,170,25,fill='white')
piece42=Circle(353,119,25,fill='white')
redList=Group()
yellowList=Group()
dashLine1=Line(22,0,22,75,fill='black',lineWidth=1,dashes=True,visible=False)
dashLine2=Line(72,0,72,75,fill='black',lineWidth=1,dashes=True,visible=False)
dashLine3=Line(123,0,123,75,fill='black',lineWidth=1,dashes=True,visible=False)
dashLine4=Line(174,0,174,75,fill='black',lineWidth=1,dashes=True,visible=False)
dashLine5=Line(225,0,225,75,fill='black',lineWidth=1,dashes=True,visible=False)
dashLine6=Line(276,0,276,75,fill='black',lineWidth=1,dashes=True,visible=False)
dashLine7=Line(327,0,327,75,fill='black',lineWidth=1,dashes=True,visible=False)
dashLine8=Line(378,0,378,75,fill='black',lineWidth=1,dashes=True,visible=False)
turnCounter=Label('yellow',200,35,size=50,bold=True,visible=False,fill='yellow',border='black')
winLine=Line(200,200,200,300,fill='black',lineWidth=5,visible=False)
winDot1=Circle(50,50,1,visible=False)
winDot2=Circle(50,50,1,visible=False)
winDot3=Circle(50,50,1,visible=False)
winDot4=Circle(50,50,1,visible=False)
winDot5=Circle(50,50,1,visible=False)
winDot6=Circle(50,50,1,visible=False)
winDot7=Circle(50,50,1,visible=False)
winDot8=Circle(50,50,1,visible=False)
winDot9=Circle(50,50,1,visible=False)
winDot10=Circle(50,50,1,visible=False)
winDot11=Circle(50,50,1,visible=False)
winDot12=Circle(50,50,1,visible=False)
winDot13=Circle(50,50,1,visible=False)
winDot14=Circle(50,50,1,visible=False)
winDot15=Circle(50,50,1,visible=False)
winDot16=Circle(50,50,1,visible=False)
winDot17=Circle(50,50,1,visible=False)
winDot18=Circle(50,50,1,visible=False)
winDot19=Circle(50,50,1,visible=False)
winDot20=Circle(50,50,1,visible=False)
winDot21=Circle(50,50,1,visible=False)
winDot22=Circle(50,50,1,visible=False)
winDot23=Circle(50,50,1,visible=False)
winDot24=Circle(50,50,1,visible=False)
winDot25=Circle(50,50,1,visible=False)
red=Rect(0,0,22,75,fill='red',visible=False)
yellow=Rect(378,0,400,75,fill='yellow',visible=False)
redWin=Label('Red Wins!',200,200,size=50,fill='red',border='black',visible=False,bold=True)
yellowWin=Label('Yellow Wins!',200,200,size=50,fill='yellow',border='black',visible=False,bold=True)
movePiece=Circle(200,200,25,fill=turnCounter.value,border='black',visible=False)
start=Rect(150,175,100,50,fill='grey',border='black',borderWidth=5,visible=True)
startWord=Label('Start',200,200,size=25,fill='white',visible=True)
title=Label('Connect 4',200,100,size=75,fill='blue',bold=True)
def winCheck(piece):
    winDot1.centerX=piece.centerX
    winDot1.centerY=piece.centerY
    winDot2.centerX=piece.centerX+51
    winDot2.centerY=piece.centerY
    winDot3.centerX=piece.centerX+102
    winDot3.centerY=piece.centerY
    winDot4.centerX=piece.centerX+153
    winDot4.centerY=piece.centerY
    winDot5.centerX=piece.centerX+51
    winDot5.centerY=piece.centerY-51
    winDot6.centerX=piece.centerX+102
    winDot6.centerY=piece.centerY-102
    winDot7.centerX=piece.centerX+153
    winDot7.centerY=piece.centerY-153  
    winDot8.centerX=piece.centerX
    winDot8.centerY=piece.centerY-51
    winDot9.centerX=piece.centerX
    winDot9.centerY=piece.centerY-102
    winDot10.centerX=piece.centerX
    winDot10.centerY=piece.centerY-153
    winDot11.centerX=piece.centerX-51
    winDot11.centerY=piece.centerY-51
    winDot12.centerX=piece.centerX-102
    winDot12.centerY=piece.centerY-102
    winDot13.centerX=piece.centerX-153
    winDot13.centerY=piece.centerY-153
    winDot14.centerX=piece.centerX-51
    winDot14.centerY=piece.centerY
    winDot15.centerX=piece.centerX-102
    winDot15.centerY=piece.centerY
    winDot16.centerX=piece.centerX-153
    winDot16.centerY=piece.centerY
    winDot17.centerX=piece.centerX-51
    winDot17.centerY=piece.centerY+51
    winDot18.centerX=piece.centerX-102
    winDot18.centerY=piece.centerY+102
    winDot19.centerX=piece.centerX-153
    winDot19.centerY=piece.centerY+153
    winDot20.centerX=piece.centerX
    winDot20.centerY=piece.centerY+51
    winDot21.centerX=piece.centerX
    winDot21.centerY=piece.centerY+102
    winDot22.centerX=piece.centerX
    winDot22.centerY=piece.centerY+153
    winDot23.centerX=piece.centerX+51
    winDot23.centerY=piece.centerY+51
    winDot24.centerX=piece.centerX+102
    winDot24.centerY=piece.centerY+102
    winDot25.centerX=piece.centerX+153
    winDot25.centerY=piece.centerY+153
    if(winDot1.hitsShape(redList) and winDot2.hitsShape(redList) and winDot3.hitsShape(redList) and winDot4.hitsShape(redList)):
        redWin.visible=True
        redWin.toFront()
    if(winDot1.hitsShape(redList) and winDot5.hitsShape(redList) and winDot6.hitsShape(redList) and winDot7.hitsShape(redList)):
        redWin.visible=True
        redWin.toFront()
    if(winDot1.hitsShape(redList) and winDot8.hitsShape(redList) and winDot9.hitsShape(redList) and winDot10.hitsShape(redList)):
        redWin.visible=True
        redWin.toFront()
    if(winDot1.hitsShape(redList) and winDot11.hitsShape(redList) and winDot12.hitsShape(redList) and winDot13.hitsShape(redList)):
        redWin.visible=True
        redWin.toFront()
    if(winDot1.hitsShape(redList) and winDot14.hitsShape(redList) and winDot15.hitsShape(redList) and winDot16.hitsShape(redList)):
        redWin.visible=True
        redWin.toFront()
    if(winDot1.hitsShape(redList) and winDot19.hitsShape(redList) and winDot18.hitsShape(redList) and winDot19.hitsShape(redList)):
        redWin.visible=True
        redWin.toFront()
    if(winDot1.hitsShape(redList) and winDot20.hitsShape(redList) and winDot21.hitsShape(redList) and winDot22.hitsShape(redList)):
        redWin.visible=True
        redWin.toFront()
    if(winDot1.hitsShape(redList) and winDot23.hitsShape(redList) and winDot24.hitsShape(redList) and winDot25.hitsShape(redList)):
        redWin.visible=True
        redWin.toFront()
    if(winDot1.hitsShape(redList) and winDot2.hitsShape(redList) and winDot3.hitsShape(redList) and winDot4.hitsShape(redList)):
        redWin.visible=True
        redWin.toFront()
    if(winDot1.hitsShape(yellowList) and winDot5.hitsShape(yellowList) and winDot6.hitsShape(yellowList) and winDot7.hitsShape(yellowList)):
        yellowWin.visible=True
        yellowWin.toFront()
    if(winDot1.hitsShape(yellowList) and winDot8.hitsShape(yellowList) and winDot9.hitsShape(yellowList) and winDot10.hitsShape(yellowList)):
        yellowWin.visible=True
        yellowWin.toFront()
    if(winDot1.hitsShape(yellowList) and winDot11.hitsShape(yellowList) and winDot12.hitsShape(yellowList) and winDot13.hitsShape(yellowList)):
        yellowWin.visible=True
        yellowWin.toFront()
    if(winDot1.hitsShape(yellowList) and winDot14.hitsShape(yellowList) and winDot15.hitsShape(yellowList) and winDot16.hitsShape(yellowList)):
        yellowWin.visible=True
        yellowWin.toFront()
    if(winDot1.hitsShape(yellowList) and winDot19.hitsShape(yellowList) and winDot18.hitsShape(yellowList) and winDot19.hitsShape(yellowList)):
        yellowWin.visible=True
        yellowWin.toFront()
    if(winDot1.hitsShape(yellowList) and winDot20.hitsShape(yellowList) and winDot21.hitsShape(yellowList) and winDot22.hitsShape(yellowList)):
        yellowWin.visible=True
        yellowWin.toFront()
    if(winDot1.hitsShape(yellowList) and winDot23.hitsShape(yellowList) and winDot24.hitsShape(yellowList) and winDot25.hitsShape(yellowList)):
        yellowWin.visible=True
        yellowWin.toFront()
#Counter Controls
def onMousePress(mouseX,mouseY):
    if(22<mouseX<72 and holder1.visible==True):
        counter1.value+=1
    if(72<mouseX<123 and holder1.visible==True):
        counter2.value+=1
    if(123<mouseX<174 and holder1.visible==True):
        counter3.value+=1
    if(174<mouseX<225 and holder1.visible==True):
        counter4.value+=1
    if(225<mouseX<276 and holder1.visible==True):
        counter5.value+=1
    if(276<mouseX<327 and holder1.visible==True):
        counter6.value+=1
    if(327<mouseX<378 and holder1.visible==True):
        counter7.value+=1
    if(150<mouseX<250 and 175<mouseY<225 and start.visible==True):
        start.visible=False
        movePiece.visible=True
        holder1.visible=True
        holder2.visible=True
        startWord.visible=False
        title.visible=False
        dashLine1.visible=True
        dashLine2.visible=True
        dashLine3.visible=True
        dashLine4.visible=True
        dashLine5.visible=True
        dashLine6.visible=True
        dashLine7.visible=True
        dashLine8.visible=True
        yellow.visible=True
        red.visible=True
        app.background='white'
#Piece Control
#Column 1
    if(22<mouseX<72 and counter1.value==1):
        piece1.fill=turnCounter.value
        addToRed(piece1)
        addToYellow(piece1)
        winCheck(piece1)
    if(22<mouseX<72 and counter1.value==2):
        piece2.fill=turnCounter.value
        addToRed(piece2)
        addToYellow(piece2)
        winCheck(piece2)
    if(22<mouseX<72 and counter1.value==3):
        piece3.fill=turnCounter.value
        addToRed(piece3)
        addToYellow(piece3)
        winCheck(piece3)
    if(22<mouseX<72 and counter1.value==4):
        piece4.fill=turnCounter.value
        addToRed(piece4)
        addToYellow(piece4)
        winCheck(piece4)
    if(22<mouseX<72 and counter1.value==5):
        piece5.fill=turnCounter.value
        addToRed(piece5)
        addToYellow(piece5)
        winCheck(piece5)
    if(22<mouseX<72 and counter1.value==6):
        piece6.fill=turnCounter.value
        addToRed(piece6)
        addToYellow(piece6)
        winCheck(piece6)
#Column 2
    if(72<mouseX<123 and counter2.value==1):
        piece7.fill=turnCounter.value
        addToRed(piece7)
        addToYellow(piece7)
        winCheck(piece7)
    if(72<mouseX<123 and counter2.value==2):
        piece8.fill=turnCounter.value
        addToRed(piece8)
        addToYellow(piece8)
        winCheck(piece8)
    if(72<mouseX<123 and counter2.value==3):
        piece9.fill=turnCounter.value
        addToRed(piece9)
        addToYellow(piece9)
        winCheck(piece9)
    if(72<mouseX<123 and counter2.value==4):
        piece10.fill=turnCounter.value
        addToRed(piece10)
        addToYellow(piece10)
        winCheck(piece10)
    if(72<mouseX<123 and counter2.value==5):
        piece11.fill=turnCounter.value
        addToRed(piece11)
        addToYellow(piece11)
        winCheck(piece11)
    if(72<mouseX<123 and counter2.value==6):
        piece12.fill=turnCounter.value
        addToRed(piece12)
        addToYellow(piece12)
        winCheck(piece12)
#Column 3
    if(123<mouseX<174 and counter3.value==1):
        piece13.fill=turnCounter.value
        addToRed(piece13)
        addToYellow(piece13)
        winCheck(piece13)
    if(123<mouseX<174 and counter3.value==2):
        piece14.fill=turnCounter.value
        addToRed(piece14)
        addToYellow(piece14)
        winCheck(piece14)
    if(123<mouseX<174 and counter3.value==3):
        piece15.fill=turnCounter.value
        addToRed(piece15)
        addToYellow(piece15)
        winCheck(piece15)
    if(123<mouseX<174 and counter3.value==4):
        piece16.fill=turnCounter.value
        addToRed(piece16)
        addToYellow(piece16)
        winCheck(piece16)
    if(123<mouseX<174 and counter3.value==5):
        piece17.fill=turnCounter.value
        addToRed(piece17)
        addToYellow(piece17)
        winCheck(piece17)
    if(123<mouseX<174 and counter3.value==6):
        piece18.fill=turnCounter.value
        addToRed(piece18)
        addToYellow(piece18)
        winCheck(piece18)
#Column 4
    if(174<mouseX<225 and counter4.value==1):
        piece19.fill=turnCounter.value
        addToRed(piece19)
        addToYellow(piece19)
        winCheck(piece19)
    if(174<mouseX<225 and counter4.value==2):
        piece20.fill=turnCounter.value
        addToRed(piece20)
        addToYellow(piece20)
        winCheck(piece20)
    if(174<mouseX<225 and counter4.value==3):
        piece21.fill=turnCounter.value
        addToRed(piece21)
        addToYellow(piece21)
        winCheck(piece21)
    if(174<mouseX<225 and counter4.value==4):
        piece22.fill=turnCounter.value
        addToRed(piece22)
        addToYellow(piece22)
        winCheck(piece22)
    if(174<mouseX<225 and counter4.value==5):
        piece23.fill=turnCounter.value
        addToRed(piece23)
        addToYellow(piece23)
        winCheck(piece23)
    if(174<mouseX<225 and counter4.value==6):
        piece24.fill=turnCounter.value
        addToRed(piece24)
        addToYellow(piece24)
        winCheck(piece24)
#Column 5
    if(225<mouseX<276 and counter5.value==1):
        piece25.fill=turnCounter.value
        addToRed(piece25)
        addToYellow(piece25)
        winCheck(piece25)
    if(225<mouseX<276 and counter5.value==2):
        piece26.fill=turnCounter.value
        addToRed(piece26)
        addToYellow(piece26)
        winCheck(piece26)
    if(225<mouseX<276 and counter5.value==3):
        piece27.fill=turnCounter.value
        addToRed(piece27)
        addToYellow(piece27)
        winCheck(piece27)
    if(225<mouseX<276 and counter5.value==4):
        piece28.fill=turnCounter.value
        addToRed(piece28)
        addToYellow(piece28)
        winCheck(piece28)
    if(225<mouseX<276 and counter5.value==5):
        piece29.fill=turnCounter.value
        addToRed(piece29)
        addToYellow(piece29)
        winCheck(piece29)
    if(225<mouseX<276 and counter5.value==6):
        piece30.fill=turnCounter.value
        addToRed(piece30)
        addToYellow(piece30)
        winCheck(piece30)
#Column 6
    if(276<mouseX<327 and counter6.value==1):
        piece31.fill=turnCounter.value
        addToRed(piece31)
        addToYellow(piece31)
        winCheck(piece31)
    if(276<mouseX<327 and counter6.value==2):
        piece32.fill=turnCounter.value
        addToRed(piece32)
        addToYellow(piece32)
        winCheck(piece32)
    if(276<mouseX<327 and counter6.value==3):
        piece33.fill=turnCounter.value
        addToRed(piece33)
        addToYellow(piece33)
        winCheck(piece33)
    if(276<mouseX<327 and counter6.value==4):
        piece34.fill=turnCounter.value
        addToRed(piece34)
        addToYellow(piece34)
        winCheck(piece34)
    if(276<mouseX<327 and counter6.value==5):
        piece35.fill=turnCounter.value
        addToRed(piece35)
        addToYellow(piece35)
        winCheck(piece35)
    if(276<mouseX<327 and counter6.value==6):
        piece36.fill=turnCounter.value
        addToRed(piece36)
        addToYellow(piece36)
        winCheck(piece36)
#Column 7
    if(327<mouseX<378 and counter7.value==1):
        piece37.fill=turnCounter.value
        addToRed(piece37)
        addToYellow(piece37)
        winCheck(piece37)
    if(327<mouseX<378 and counter7.value==2):
        piece38.fill=turnCounter.value
        addToRed(piece38)
        addToYellow(piece38)
        winCheck(piece38)
    if(327<mouseX<378 and counter7.value==3):
        piece39.fill=turnCounter.value
        addToRed(piece39)
        addToYellow(piece39)
        winCheck(piece39)
    if(327<mouseX<378 and counter7.value==4):
        piece40.fill=turnCounter.value
        addToRed(piece40)
        addToYellow(piece40)
        winCheck(piece40)
    if(327<mouseX<378 and counter7.value==5):
        piece41.fill=turnCounter.value
        addToRed(piece41)
        addToYellow(piece41)
        winCheck(piece41)
    if(327<mouseX<378 and counter7.value==6):
        piece42.fill=turnCounter.value
        addToRed(piece42)
        addToYellow(piece42)
        winCheck(piece42)
    if(turnCounter.value=='red'):
        turnCounter.value='yellow'
    else:
        turnCounter.value='red'
    movePiece.fill=turnCounter.value
    turnCounter.fill=turnCounter.value
def onMouseMove(mouseX,mouseY):
    movePiece.centerX=mouseX
    movePiece.centerY=mouseY
def onMouseDrag(mouseX,mouseY):
    movePiece.centerX=mouseX
    movePiece.centerY=mouseY
cmu_graphics.run()
