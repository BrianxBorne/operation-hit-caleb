import numpy as np
import matplotlib.pyplot as plt
import os
import random

def projectile_motion(v0, theta, total_time, k, caleb_x, caleb_width, caleb_top=50, time_step=0.01):
    g = 9.81
    theta_rad = np.radians(theta)
    v0x = v0 * np.cos(theta_rad)
    v0y = v0 * np.sin(theta_rad)
    
    x_vals, y_vals = [0], [0]
    vx, vy = v0x, v0y
    t = 0
    
    while t < total_time and y_vals[-1] >= 0:
        drag_x = -k * vx
        drag_y = -k * vy
        
        vx += drag_x * time_step
        vy += (-g + drag_y) * time_step
        
        x_prev, y_prev = x_vals[-1], y_vals[-1]
        x_new = x_prev + vx * time_step
        y_new = y_prev + vy * time_step
        
       
        if y_prev > caleb_top and y_new <= caleb_top:
           
            if caleb_x <= x_new <= (caleb_x + caleb_width):
               
                ratio = (y_prev - caleb_top) / (y_prev - y_new)
                x_hit = x_prev + ratio * (x_new - x_prev)
                x_vals.append(x_hit)
                y_vals.append(caleb_top)
                break
        
        x_vals.append(x_new)
        y_vals.append(y_new)
        t += time_step

    return x_vals, y_vals

def save_plot(x_vals, y_vals, caleb_x, caleb_width, caleb_top=50):
    output_dir = "output"
    os.makedirs(output_dir, exist_ok=True)
    
    plt.figure(figsize=(10, 5))
    plt.plot(x_vals, y_vals, label="Stone Projectile", color="red")
    
    plt.gca().add_patch(plt.Rectangle((caleb_x, 0), caleb_width, caleb_top, color='blue', alpha=0.3, label="Caleb"))
    plt.xlabel("Horizontal Distance (m)")
    plt.ylabel("Vertical Height (m)")
    plt.title("OPERATION HIT CALEB")
    plt.legend()
    plt.grid(True)
    
    file_path = os.path.join(output_dir, "stone_caleb.png")
    plt.savefig(file_path, dpi=300)
    print(f"\n▶ The graph picture is saved at: {file_path} as 'stone_caleb.png'.")

def main():
    print("WELCOME TO OPERATION HIT CALEB")
    
    print("Caleb has stolen your walet and is running away with it")
    print("""⠀⠀⠀⠀⠀          ⠀⣠⠤⠤⣀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠁⡄⠀⢈⡆⠀⢀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣈⣆⠱⡀⢠⠓⢀⠀⠀⡤⡀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠤⠖⠒⠲⠉⠉⠘⡗⠺⡉⠀⠀⢰⠶⠀⡇⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⡎⠀⢠⣀⣀⣀⢤⠤⠀⡜⠀⢹⡀⠀⣀⠀⡔⠁⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠘⡇⠀⠸⠀⠀⠸⡀⠈⠉⠀⠄⠈⡇⠉⢀⠎⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢡⠀⡇⠀⠀⠀⢣⠀⠀⠀⠀⠀⡧⠔⠋⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢈⣄⡇⠀⠀⢀⡼⠀⠀⠀⠀⢸⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠀⢨⠆⢀⠎⠀⠀⠀⠀⣠⠃⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠣⠸⠀⠸⠈⠉⠀⠈⠁⠈⠉⠒⠶⢤⣀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠇⠸⣄⠀⠀⠀⠀⠀⢀⠃⠀⠈⠑⢦⡀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡮⢄⡀⠈⢙⡶⠲⠦⠤⠮⠔⡶⠂⠀⠀⡇
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡸⠀⠀⠈⣩⠞⠀⠀⠀⠀⠀⢸⠀⠀⠀⡜⠁
       ⠀⠀⣠⠖⠒⠃⠀⣠⠚⠁⠀⠀⠀⠀⠀⠀⡜⠀⢀⠎⠀⠀
⠀⠀⠀⠀⠀⠀⡠⠊⠀⠀⣀⡠⠔⠁⠀⠀⠀⠀⠀⠀⠀⡔⠀⡠⠁⠀⠀⠀
⠀⢀⠤⡤⠔⠈⢀⡠⠖⠋⠁⠀⠀⠀⠀⠀⠀⠀⢀⠤⢎⣀⠜⠀⠀⠀⠀⠀
⠀⠸⠀⢇⠠⠂⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠲⢄⠀⠙⡄⠀⠀⠀⠀
⢠⠃⢠⠊⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠑⢄⡈⢢⠀⠀⠀
⠈⠢⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀""")
    print("You are about to throw a stone with the sole aim of hitting Caleb")

    
    
    stone_mass = float(input("\nChoose your stone. What is the mass of the stone (in kg)? "))
    
   
    v0 = float(input("How fast should we throw the stone? (Enter initial velocity in m/s): "))
    theta = float(input("At what angle should it soar? (Enter launch angle in degrees): "))
    total_time = float(input("For how long should we monitor the stone? (Enter simulation time in seconds): "))
    
   
    k = random.uniform(0.0, 0.3)
   
    caleb_x = random.uniform(500, 900)
   
    caleb_width = 20.0
    
    print(f"\nUnpredictable conditions: Air resistance factor is {k:.2f}, and Caleb is chilling between x = {caleb_x:.2f} m and {caleb_x+caleb_width:.2f} m!")
    
    
    dt = 0.2
    force = stone_mass * (v0 / dt)  
    
    print(f"\nThrowing in 3... 2... 1... Stone is moving at {v0:.2f} m/s, weighing {stone_mass:.2f} kg,")
    print(f"with an estimated force of {force:.2f} N\n")
    print(f"""                                                                                                   
                                                            
                                   █████                    
                                █         █                 
                               █  █                         
                                    █   █                   
                             █              █               
                              █        █    █               
                               █                            
                       █ █       █    ██ ██                 
                     █ █           █████                    
                    ██    ███                               
                  ██     ██                                 
                       ███     ██                           
                     ███     ███                            
                   ███     ███                              
                  ██      ██                                
                ██      ██          
                                                                                                                                 
                                                                                             """)
    x_vals, y_vals = projectile_motion(v0, theta, total_time, k, caleb_x, caleb_width, caleb_top=50)
    
    print("The simulation is complete. Check the graph to see if your stone managed to hit Caleb.")
    save_plot(x_vals, y_vals, caleb_x, caleb_width, caleb_top=50)

if __name__ == "__main__":
    main()
