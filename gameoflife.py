import numpy as np
import pygame 
import time

color_base = (0, 0, 0)
color_grid = (40, 40, 40)
color_alive = (0, 255, 0)

def update(screen, cells, cell_size, gameon = False):
    live_grid = np.zeros((cells.shape[0],cells.shape[1]))

    for i,j in np.ndindex(cells.shape):
        alive = np.sum(cells[i-1:i+2, j-1:j+2]) - cells[i,j]
        if cells[i,j] == 0:
             color = color_base 
        else:
            color = color_alive

        if cells[i,j] == 1:
            
            if alive <= 1 or alive >3:
                live_grid[i,j] = 0
                if gameon:
                    color = color_base

            elif 2 <= alive <= 3:
                live_grid[i,j] = 1
                if gameon:
                    color = color_alive

        else:
            if alive == 3:
                live_grid[i,j] = 1
                if gameon:
                    color = color_alive   

        pygame.draw.rect(screen, color, (i * cell_size, j * cell_size, cell_size-1, cell_size-1)) 
    
    return live_grid        
 
def main():
    pygame.init()
    sizeh = 800
    sizev = 600
    screen = pygame.display.set_mode((sizeh,sizev))
    rows = 60
    n = sizev//rows
    columns = sizeh//n
    
    cells = np.zeros((rows, columns))
    screen.fill(color_grid)
    update(screen, cells, n)

    pygame.display.update()

    
    count = 0
    running = False
    init = [(14, 15)]
    
    #for k,l in init:
        #cells[k-1 , l-1] = 1
        #update(screen, cells, n)
        #pygame.display.update() 

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT :
                pygame.quit()
                return
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    running = not running  
                    update(screen, cells, n)
                    pygame.display.update()
                elif event.key == pygame.K_g:
                    for o,p in np.ndindex(cells.shape):
                        cells[o,p] = np.random.randint(0,2)
                    update(screen, cells, n)
                    pygame.display.update()
                elif event.key == pygame.K_z:
                    for l,m in np.ndindex(cells.shape):
                            cells[l,m] = 0
                    update(screen, cells, n)
                    pygame.display.update()
            if pygame.mouse.get_pressed()[0]:
                    position = pygame.mouse.get_pos() 
                    cells[position[0] // n, position[1] // n] = 1
                    update(screen, cells, n)
                    pygame.display.update()
            elif pygame.mouse.get_pressed()[2]:
                    position = pygame.mouse.get_pos() 
                    cells[position[0] // n, position[1] // n] = 0
                    update(screen, cells, n)
                    pygame.display.update()
            
            
                    

        screen.fill(color_grid)

        if running: 
            cells = update(screen, cells, n)
            count += 1
            pygame.display.update() 

        time.sleep(0.01)    

if __name__ == "__main__":
    main()     
