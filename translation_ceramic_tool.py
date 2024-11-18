#Translation of a sentence into a 3D tool for ceramic based on the ASCII chart

source = "Hello, world"


count0 = 0
count1 = 0

x = 0
y = 0

prog_x = 2
prog_y = 2

def main():
    global count0, count1, x, y, prog_x, prog_y
    #create a list of ascii values
    ascii_values = [ord(char) for char in source]
    for value in ascii_values:
        value_to_binary(value)
        #move the y coordinate
        y += prog_y
        #reset x to 0
        x = 0
    print(f'count 1 = {count1}')
    print(f'count 0 = {count0}')
    print(f'x = {x}')
    print(f'y = {y}')

def value_to_binary (n):
    global count0, count1, x, y, prog_x, prog_y
    binary_string = format(n, '08b')
    for digit in binary_string:
        #print(digit, end="")
        if(int(digit) == 1):
            print("X", end="")
            count1 += 1
            #generate a cylinder
            #so 1s are eventually holes in the ceramic object
            bpy.ops.view3d.pastebuffer()
            bpy.ops.transform.translate(value=(x, y, 0), orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', constraint_axis=(False, True, False), mirror=False, use_proportional_edit=False, proportional_edit_falloff='SMOOTH', proportional_size=1, use_proportional_connected=False, use_proportional_projected=False, snap=False, snap_elements={'INCREMENT'}, use_snap_project=False, snap_target='CLOSEST', use_snap_self=True, use_snap_edit=True, use_snap_nonedit=True, use_snap_selectable=False)
        else:
            print(" ", end="")
            count0 += 1
        #move the x coordinate
        x += prog_x
    print()

main ()