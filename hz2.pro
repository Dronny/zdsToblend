TEMPLATE = app
CONFIG += console
CONFIG -= app_bundle
CONFIG -= qt

SOURCES += main.cpp

CCFLAG += -std=c++11 -flto -Os -s -m32 -mtune=atom -fno-common -fno-exceptions -fno-ident  -ffunction-sections, -Wl,--gc-sections --strip-all #-fno-rtti
win32:QMAKE_CXX += -std=c++11 -flto -Os -s -m32 -mtune=i386 -fno-common -fno-exceptions -fno-ident -ffunction-sections -Wl,--gc-sections  #-fno-rtti
unix:QMAKE_CXX += -std=c++11 -flto -Os -s -m32 -mtune=atom -fno-common -fno-exceptions -fno-ident -ffunction-sections -Wl,--gc-sections  #-fno-rtti

QMAKE_LFLAGS += -s

win32:QMAKE += -std=c++11 -flto -Os -s -m32 -mtune=i386 -fno-common -fno-exceptions -fno-ident -ffunction-sections, -Wl,--gc-sections --strip-all #-fno-rtti
win32:LIBS += -lmingw32 -lSDLmain -lSDL  -mwindows  -lm -luser32 -lgdi32 -lwinmm -ldxguid
unix:QMAKE += -std=c++11 -flto -Os -s -m32 -mtune=atom -fno-common -fno-exceptions -fno-ident -ffunction-sections, -Wl,--gc-sections --strip-all #-fno-rtti
unix:LIBS += -lSDL
