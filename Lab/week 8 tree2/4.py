"""

Jean รักษาการผู้บัญชาการของกองอัศวิน Favonius แห่ง Mondstadt ต้องการทราบถึงขุมพลังของอัศวินในแต่ละกลุ่มภายในเมือง Mondstadt 
แห่งนี้จึงจะทดสอบความแข็งแกร่งของขุมกำลังที่มี โดยจะทำการจัดวางกำลังอัศวินภายในเมือง Mondstadt ดังตัวอย่างต่อไปนี้
                พลัง    :   5  4  4  3  2  2  2
                ลำดับ  :   0  1  2  3  4  5  6
จากข้อมูลข้างต้นประกอบด้วยอัศวินทั้งหมด 7 คน เรียงตามลำดับตั้งแต่ลำดับที่ 0 ถึง 6 และพลังของอัศวินแต่ละคนมีข้อกำหนดดังนี้
    -  อัศวินลำดับที่ n จะมีลูกน้องในสังกัดอยู่ลำดับที่ 2n+1 และ 2n+2 (ลูกน้องของลูกน้องของอัศวินลำดับที่ n ถือว่าเป็นลูกน้องของอัศวินลำดับที่ n ด้วย)
    -  ค่าพลังของอัศวินมีค่าตั้งแต่ 0 - 5
    -  กลุ่มของอัศวินกลุ่มที่ i จะมีสมาชิกคือ อัศวินลำดับที่ i และลูกน้องของอัศวินลำดับที่ i (รวมลูกน้องของลูกน้องของอัศวินด้วย)
    -  พลังของกลุ่มอัศวินลำดับที่ i เป็นพลังรวมของสมาชิกของอัศวินทั้งหมดในกลุ่ม เช่น
            -  อัศวินกลุ่มที่ 1 หมายถึง กลุ่มของอัศวินลำดับที่ 1 ซึ่งมีสมาชิกประกอบด้วย อัศวินลำดับที่ 1, 3 และ 4 และค่าพลังรวมของอัศวินกลุ่มที่ 1 เท่ากับ 4 + 3 + 2 = 9
            -  อัศวินกลุ่มที่ 2 หมายถึง กลุ่มของอัศวินลำดับที่ 2 ซึ่งมีสมาชิกประกอบด้วย อัศวินลำดับที่ 2 , 5 และ 6 และค่าพลังรวมของอัศวินกลุ่มที่ 2 เท่ากับ 4 + 2 + 2 = 8

ดังนั้นเมื่อนำพลังของอัศวินกลุ่มที่ 1 และ 2 มาเทียบกัน จะได้ว่าพลังรวมของอัศวินกลุ่มที่ 1 นั้นมากกว่าพลังรวมของอัศวินกลุ่มที่ 2
Jean ต้องการทราบว่าค่าพลังรวมของอัศวินภายในเมือง Mondstadt เป็นเท่าใด และถ้าเปรียบเทียบระหว่างอัศวินแต่ละกลุ่มแล้วค่าของพลังรวมของอัศวินในกลุ่มใดมีค่ามากกว่ากัน

Enter Input : 5 4 4 3 2 2 2/1 2,5 6,2 0
22
1>2
5=6
2<0

Enter Input : 4 5/0 1,1 0
9
0>1
1<0

"""

class ArrayBST:
    def __init__(self, lst=None):
        if lst is None:
            self.items = []
        else:
            self.items = lst

    def get_left_child_index(self, index):
        l_index = index*2+1
        return l_index if l_index < self.size() else -1

    def get_right_child_index(self, index):
        r_index = index*2+2
        return r_index if r_index < self.size() else -1

    def size(self):
        return len(self.items)

    def sum_power(self, init=0):  # bfs style
        queue = []
        value = 0
        queue.append(init)
        while len(queue) > 0:
            curr = queue.pop(0)
            # print(curr)
            if 0 <= curr < self.size():
                value += self.items[curr]
                l_child = self.get_left_child_index(curr)
                r_child = self.get_right_child_index(curr)
                # print(l_child, r_child)
                if l_child != -1:
                    queue.append(l_child)
                if r_child != -1:
                    queue.append(r_child)
                # print(queue)
            # print('-------------------------')
        return value

    def compare_power(self, root_a, root_b):
        a_power = self.sum_power(root_a)
        b_power = self.sum_power(root_b)
        if a_power > b_power:
            print(f'{root_a}>{root_b}')
        elif a_power < b_power:
            print(f'{root_a}<{root_b}')
        else:
            print(f'{root_a}={root_b}')

    def __str__(self):
        return str(self.items)



inp = input('Enter Input : ').split('/')
initial_list = list(map(int, inp[0].split()))
compare_list = inp[1].split(',')
tree = ArrayBST(initial_list)
print(tree.sum_power())
for pair in compare_list:
  a, b = tuple(map(int, pair.split()))
  tree.compare_power(a, b)