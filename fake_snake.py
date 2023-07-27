#size adjustments need to be int(), annoying errors keep popping up
from games import *
import random

display.set_caption("Fake Snake!") #title


def draw_rect(x, y): #draws snake
    draw.rect(screen, GREEN, [x, y, 20, 20], 0)
def draw_rect_f(x, y): #draws food
    draw.rect(screen, RED, [x, y, 20, 20], 0)
def unpause(paused): #unpauses game
    paused=False
    return paused
def pause(): #pause screen
    size=pygame.display.get_surface().get_size() 
    paused=None
    x=1
    y=1
    while paused==None:    
        pos_mouse= mouse.get_pos()
        x_mouse=pos_mouse[0]
        y_mouse=pos_mouse[1]
        screen = display.set_mode(size,RESIZABLE)
        for event in pygame.event.get():
            if event.type==VIDEORESIZE:
                screen=pygame.display.set_mode(event.dict['size'],HWSURFACE|DOUBLEBUF|RESIZABLE)
                size=pygame.display.get_surface().get_size()
                pygame.display.flip()
            if event.type == QUIT: # If user clicked close
                quitgame()
                # Flag that we are done so we exit this loop
            if event.type== KEYDOWN and event.key==K_ESCAPE:
                paused=False
            

        draw.rect(screen, GREY, [300,100,300,400]) #size
        pause_txt=draw_text("Paused", 'calibri', 35, RED) #size maybe
        pause_txt_w=pause_txt[1]
        screen.blit(pause_txt[0], [(size[0]-pause_txt_w)/2, size[1]*5/28])
        paused=button("continue",size[0]*4/9,size[1]*2/7,size[0]/9,size[1]/36,GREEN,BLACK,unpause,paused)#size  
        button("quit",size[0]*4/9,size[1]*4/7,size[0]/9,size[1]/36,RED,BLACK,quitgame) #size
        button("Restart", size[0]*4/9, size[1]*3/7, size[0]/9,size[1]/36, YELLOW, BLACK, main) #size
        
        display.flip()
     
        
        clock.tick(60)
def intro():  #intro screen
    done = False
    while not done:    
        
        for event in pygame.event.get():
            if event.type==VIDEORESIZE:
                screen=pygame.display.set_mode(event.dict['size'],HWSURFACE|DOUBLEBUF|RESIZABLE)
                size=pygame.display.get_surface().get_size()
                pygame.display.flip()
            if event.type == QUIT: # If user clicked close
                done = True # Flag that we are done so we exit this loop
            if event.type== KEYDOWN and event.key==K_ESCAPE:
                done= True
        screen.fill(BLACK)
        title= draw_text("Fake Snake", 'Calibri', 50, GREEN)   #size maybe font
        title_w=title[1]
        screen.blit(title[0], [(size[0]-title_w)/2, size[1]/14]) 
        button("Start",size[0]*3/9,size[1]*6/7,size[0]/9,50,GREEN,BLACK, main) #size
        button("quit",size[0]*5/9,size[1]*6/7,size[0]/9,50,RED,BLACK,quitgame) #size
        
        display.flip()
     
        # --- Limit to 60 frames per second
        clock.tick(60)
def finish( main_done): #lose screen #get rid of main_done variable which isn't used
    finish_done=False
    size=pygame.display.get_surface().get_size()
    screen = display.set_mode(size,RESIZABLE)
    while not finish_done:
        
        for event in pygame.event.get():
            if event.type==VIDEORESIZE:
                screen=pygame.display.set_mode(event.dict['size'],HWSURFACE|DOUBLEBUF|RESIZABLE)
                size=pygame.display.get_surface().get_size()
                pygame.display.flip()
            if event.type== KEYDOWN and event.key==K_RETURN:
                main()
            if event.type == QUIT: # If user clicked close
                quitgame()
                # Flag that we are done so we exit this loop
            if event.type== KEYDOWN and event.key==K_ESCAPE:
                quitgame()
        lose=draw_text("Game Over", 'calibri', 35, RED) #size maybe
        lose_w=lose[1]
        screen.blit(lose[0], [(size[0]-lose_w)/2, size[1]*5/14])
        button("quit",size[0]*4/9,size[1]*4/7,size[0]/9,size[1]/28,RED,BLACK,quitgame) #size
        button("Restart", size[0]*4/9, size[1]*3/7, size[0]/9,size[1]/28,YELLOW, BLACK, main) #size
        display.flip()
     
        # --- Limit to 60 frames per second
        clock.tick(60)
def eat(s_posx, s_posy,f_posx, f_posy):  #snake eats food and alows snake to grows
    eaten=False
    s_cent=(s_posx+15, s_posy+15)
    f_cent=(f_posx+15, f_posy+15)
    if s_cent==f_cent:
        return True
def crash(coord_list): #crash detection into itself
    for i in range(len(coord_list)-1):
        if coord_list[-1]== coord_list[i]:
            return True
def turn(direction,result,coord_list,main_done,x_speed,y_speed,direc,opp,nxspeed,nyspeed): #main returns all variables in a list, call main[x]   controls moving 
    if direction!=opp:
        x_speed =nxspeed #size
        y_speed=nyspeed 
        direction=direc
    else:
        if len(coord_list)>1:  # alllows crash when only two squares long
            result=True
        else:
            x_speed =x_speed #size
            y_speed=y_speed 
            direction=direc
    if result==True:
        finish(main_done)
    return (direction,result,x_speed,y_speed)
def main(): #actual game
    main_done = False
    finsih=False
    snake_w=20
    x_speed = 0 #size
    y_speed = 0 #size
    x_coord = 60
    y_coord = 0
    ate=False
    size=pygame.display.get_surface().get_size() #used to resize screen
    coord_list=[(x_coord,y_coord)]
    fx=random.randrange(0, 881,20) #randomly places food
    fy=random.randrange(0,681,20)
    direction=""
    screen = display.set_mode(size,RESIZABLE)
    while not main_done:
        speed=size[1]*2/70   #700/1017  900/1920
        # --- Main event loop
        for event in pygame.event.get():
            if event.type==VIDEORESIZE:
                screen=pygame.display.set_mode(event.dict['size'],HWSURFACE|DOUBLEBUF|RESIZABLE)
                size=pygame.display.get_surface().get_size()
                pygame.display.flip()
            if event.type == QUIT: # If user clicked close
                quitgame()
                # Flag that we are done so we exit this loop
            if event.type== KEYDOWN and event.key==K_ESCAPE:
                quitgame()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    pause()
                if event.key == pygame.K_a or event.key ==pygame.K_LEFT:  #keep direction say if direction = oppisite say no
                    state=turn(direction,result,coord_list,main_done,x_speed,y_speed,"left","right",-speed,0)
                    direction,result,x_speed,y_speed=state
                if event.key == pygame.K_d or event.key ==pygame.K_RIGHT:
                    state=turn(direction,result,coord_list,main_done,x_speed,y_speed,"right","left",speed,0)
                    direction,result,x_speed,y_speed=state
                if event.key == pygame.K_w or event.key ==pygame.K_UP:
                    state=turn(direction,result,coord_list,main_done,x_speed,y_speed,"up","down",0,-speed)
                    direction,result,x_speed,y_speed=state
                if event.key == pygame.K_s or event.key ==pygame.K_DOWN:
                    state=turn(direction,result,coord_list,main_done,x_speed,y_speed,"down","up",0,speed)
                    direction,result,x_speed,y_speed=state
        screen.fill(BLACK)
        f_x=random.randrange(0, int(size[0]-speed+1),int(speed)) #size
        f_y=random.randrange(0,int(size[1]-speed+1),int(speed)) #size
        draw_rect_f(fx, fy)  
        
        eaten=eat(x_coord, y_coord, fx, fy)
         #can't subtract 20 for both x and y
            #snake_len+=1

        
    # moves snake forward
        x_coord += x_speed
        y_coord += y_speed
        
       # allows for wraparound screen
        if x_coord >= 900: #size
            x_coord=0
        if x_coord<=-20: #size
            x_coord=880 #size
        if y_coord>=700: #size
            y_coord=0
        if y_coord<=-20: #size
            y_coord=680 #size
        if finsih!= True:
            coord_list.append((x_coord,y_coord)) #updates coord list of snake
            coord_list.pop(0) #need
            #respawns food in new place
        if eaten==True:    #change eaten but can't assign eaten in loop but you have too to update coords 
            f_x=random.randrange(0, 881,20) #size
            f_y=random.randrange(0,681,20) #size
            fx=f_x
            fy=f_y
            #adds new snake portion in coord list
            if x_speed==0 and y_speed==20: #down   #size
                coord_list.insert(0,((coord_list[0][0],coord_list[0][1]-20))) #size
            if x_speed==0 and y_speed==-20: #up  #size
                coord_list.insert(0,((coord_list[0][0],coord_list[0][1]+20))) #size
            if x_speed==20 and y_speed==0: #right   #size
                coord_list.insert(0,((coord_list[0][0]-20,coord_list[0][1]))) #size
            if x_speed==-20 and y_speed==0: #left    #size
                coord_list.insert(0,((coord_list[0][0]+20,coord_list[0][1]))) #size
            ate=True        
        
        if ate==True:  #Can't eat second more than one food, can still eat invisible first food.
            draw_rect_f(fx, fy)  
         
        for i in range(len(coord_list)):  #Draws Snake
            draw_rect( coord_list[i][0],coord_list[i][1])

        result=crash(coord_list) #checks to see if there is a crash
        if result==True:
            finish(main_done)
        #print(size) (1920, 1057), max size, (900,700), normal size
        for i in range(size[0]):
            draw
        display.flip()
        
        
        # --- Limit to 60 frames per second
        clock.tick(10) #size for speed and moving if I want to follow Dugan, no
intro()
quit()
