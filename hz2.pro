TEMPLATE = app
CONFIG += console
CONFIG -= app_bundle
CONFIG -= qt

SOURCES += main.cpp
CCFLAG += -std=c++11 -flto -Os -s -m32 -mtune=atom -fno-common -fno-exceptions -fno-ident  -ffunction-sections, -Wl,--gc-sections --strip-all #-fno-rtti
QMAKE_CXX += -std=c++11 -flto -Os -s -m32 -mtune=atom -fno-common -fno-exceptions -fno-ident -ffunction-sections -Wl,--gc-sections  #-fno-rtti
QMAKE_LFLAGS += -s
QMAKE += -std=c++11 -flto -Os -s -m32 -mtune=atom -fno-common -fno-exceptions -fno-ident -ffunction-sections, -Wl,--gc-sections --strip-all #-fno-rtti
LIBS += -lSDL

