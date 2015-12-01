#include <cstdlib>
#include <SDL/SDL.h>


const Uint32 FRAME_TIME = 1000/60;
void drawPixel(SDL_Surface * screen,int x, int y, SDL_Color color );


class drawableBitmap  //static pics
{ public:
    char color = 1;
    char size = 32;
    int32_t position = 0;
    bool * BitmapPointer;
    SDL_Surface * pSurface = NULL;
    drawableBitmap(SDL_Surface * surface,bool* pointer,char size_i, int32_t position) noexcept{
        this->pSurface = surface;this->size = size_i;this->position = position;
        this->BitmapPointer = pointer; }
    ~drawableBitmap() noexcept{
        delete this->BitmapPointer;
        delete this->pSurface;
    }
    void draw(){

    }
};


int main(int argc, char *argv[])
{
    SDL_Init(SDL_INIT_VIDEO);
    SDL_Surface * screen = SDL_SetVideoMode(640,480,0,SDL_ANYFORMAT);
    SDL_Event event;
    if (screen != NULL){printf("\nSURFACE CREATED...\n");}
    SDL_FillRect(screen,NULL,SDL_MapRGB(screen->format,0,0,255));
    //MAIN LOOP
    srand([=](){ auto t = 0;fgets((char*) &t,sizeof(t),fopen("/dev/random","r")); return t;}());
    for (;;){
        for (int i = 0;i < 100;i++) {drawPixel(screen,rand()%640,rand()%480, SDL_Color {(Uint8)(rand()%255),(Uint8)(rand()%255),(Uint8)(rand()%255),0});};
        SDL_UpdateRect(screen,0,0,0,0);
        //EVENTS HERE
            if (SDL_PollEvent(&event) == 0){}
            else{if(event.type == SDL_QUIT)break;}
                 if (event.type == SDL_KEYDOWN){
                     if (event.key.keysym.sym == SDLK_LEFT){printf("\nworked\n");}
                 };
    }

    SDL_FreeSurface(screen);
    SDL_Quit();
    printf("\nGoodbuy\n");
    return 0;
}

void drawPixel(SDL_Surface *screen, int x, int y, SDL_Color color){
    auto draw = [=](){Uint32 scrColor = SDL_MapRGB(screen->format,color.r,color.g,color.b);
                        memcpy((char*) screen->pixels+x*screen->format->BytesPerPixel+y*screen->pitch,&scrColor,screen->format->BytesPerPixel);};
    if (SDL_MUSTLOCK(screen)){if(SDL_LockSurface(screen) == -1){exit(1);}else{draw();SDL_UnlockSurface(screen);}}
    else{draw();}
}


