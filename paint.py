import pygame
import sys

sys.setrecursionlimit(10000)

pygame.init()
screen = pygame.display.set_mode ([800, 650])

# 0 - värvipliiats, 1 - värvipott
#Floodfill

current_tool = 0
current_color = [255, 255, 255]
mouse_down = False

brush_icon = pygame.image.load("Brush.png")
paintcan_icon = pygame.image.load("Can.png")


def quit():
    pygame.quit()
    sys.exit()

def tool_bar(screen,):
    screen.fill ([150, 150, 150], [0, 600, 800, 50])
    if current_tool == 0:
        screen.blit(brush_icon, [20, 605])
    else:
        screen.blit(brush_icon, [20, 605])

    if current_tool == 1:
        screen.blit(paintcan_icon, [65, 605])
    else:
        screen.blit(paintcan_icon, [65, 605])

    
    screen.fill ([230, 0, 0], [110, 605, 40, 40])
    screen.fill ([0, 230, 0], [155, 605, 40, 40])
    screen.fill ([0, 0, 230], [200, 605, 40, 40])

def fill (node, target_color, replacement_color, screen, visited):

    visited.append(node)

    

    if target_color == replacement_color:
        return


    if screen.get_at (node) != target_color:
        return
    
    elif screen.get_at(node) == target_color:
        screen.set_at(node, replacement_color)

        if not [node[0], node[1]-1] in visited and node[1] >= 0:
            fill ([node[0], node[1]-1], target_color, replacement_color, screen, visited)
        if not [node[0], node[1]+1] in visited and node[1] < 800:
            fill ([node[0], node[1]+1], target_color, replacement_color, screen, visited)
        if not [node[0]-1, node[1]] in visited and node[0] >= 0:    
            fill ([node[0]-1, node[1]], target_color, replacement_color, screen, visited)
        if not [node[0]+1, node[1]] in visited and node[0] < 600:    
            fill ([node[0]+1, node[1]], target_color, replacement_color, screen, visited)

    return

def tool_handle (event):
    global current_tool, current_color, mouse_down, pos, screen
    
    if event.type == pygame.MOUSEBUTTONDOWN:
        pos = pygame.mouse.get_pos()

        nupp1 = pygame.Rect ([20, 605, 40, 40])
        nupp2 = pygame.Rect ([65, 605, 40, 40])
        nupp3 = pygame.Rect ([110, 605, 40, 40])
        nupp4 = pygame.Rect ([155, 605, 40, 40])
        nupp5 = pygame.Rect ([200, 605, 40, 40])

        sheet = pygame.Rect ([0, 0, 800, 600])

    

        if nupp1.collidepoint(pos):
            current_tool = 0
            print(current_tool, current_color)

        elif nupp2.collidepoint (pos):
            current_tool = 1
            print(current_tool, current_color)

        elif nupp3.collidepoint (pos):
            current_color = [255, 0, 0]
            print(current_tool, current_color)

        elif nupp4.collidepoint (pos):
            current_color = [0, 255, 0]
            print(current_tool, current_color)

        elif nupp5.collidepoint (pos):
            current_color = [0, 0, 255]
            print(current_tool, current_color)

        elif sheet.collidepoint(pos) and current_tool == 0:
            mouse_down = True

        elif sheet.collidepoint(pos) and current_tool == 1:
            fill(pos, screen.get_at(pos), current_color, screen, [])

        
    elif event.type == pygame.MOUSEBUTTONUP:
        mouse_down = False


if __name__ == "__main__":
    pos = None
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()

            else:
                tool_handle(event)

        if mouse_down:
            if pos == None:
                pos2 = pygame.mouse.get_pos()
            else:
                pos2 = pos
            pos = pygame.mouse.get_pos()
            pygame.draw.circle(screen, current_color, pos, 4)
            pygame.draw.line(screen, current_color, pos, pos2, 8)

        tool_bar(screen)
        pygame.display.flip()
