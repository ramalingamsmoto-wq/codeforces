import sys

input = lambda: sys.stdin.readline().rstrip()

# Short aliases for common input types
ii = lambda: int(input())                    # Single integer
mi = lambda: map(int, input().split())       # Multiple integers (unpacking)
li = lambda: list(map(int, input().split())) # List of integers
si = lambda: input()                         # Single string
ls = lambda: input().split()                 # List of strings

def is_sorted(lst):
    return all(lst[i] <= lst[i + 1] for i in range(len(lst) - 1))
  
def get_monotonic_segments(arr):
  if len(arr) < 2:
    return []

  segments = []
  start = 0
  direction = None  # 'inc' or 'dec'

  for i in range(1, len(arr)):
    if arr[i] > arr[i - 1]:
      curr_dir = 'inc'
    elif arr[i] < arr[i - 1]:
      curr_dir = 'dec'
    else:
      curr_dir = None

    if curr_dir != direction:
      # Save the previous valid segment before switching
      if direction is not None:
        segments.append((start, i - 1, direction))

      # If moving into a new trend, it starts at the previous element (i - 1)
      start = i - 1 if curr_dir is not None else i
      direction = curr_dir

  # Append the final active segment at the end of the loop
  if direction is not None:
    segments.append((start, len(arr) - 1, direction))

  return segments


# Example
#nums = [1, 3, 5, 4, 2, 2, 6, 8]
#print(get_monotonic_segments(nums))
# Output: [(0, 2, 'inc'), (2, 4, 'dec'), (5, 7, 'inc')]


def process(n,a):
    tup=()
    if is_sorted(a):
        tup=("yes",1,1)
    else:
        b=[]    
        for i in range(n):
            tup1=(i+1,a[i])
            b.append(tup1)
        sb= sorted(b, key=lambda x: x[1])
        bi=[]
        for i in range(n):
            bi.append(sb[i][0])
            
        segs=get_monotonic_segments(bi)
        #print(f" bi {bi}")
        #print(f"segs {segs}")
        if len(segs)<=2:
            
            start=-1
            end=-1
            if len(segs)==1:
                start=segs[0][0]
                end=segs[0][1]
                tup=("yes",start+1,end+1)
                
            elif len(segs)==2:    
                if segs[0][2]=="dec":
                    start=segs[0][0]
                    end=segs[0][1]
                else:
                    start=segs[1][0]  
                    end=segs[1][1]  
                tup=("yes",start+1,end+1)   
        else:
            tup=("no",)    
             
    return tup        
            
        
        
                
        
        
        
        
    
n=ii()
a=li()
tup=process(n,a)
if tup[0]=="no":
    print(tup[0])
else:
    print(tup[0])   
    print(f"{tup[1]} {tup[2]}") 
    