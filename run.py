# replace these
from strategies.tit_for_tat import play as A_STRAT
from strategies.always_collab import play as B_STRAT

# point system is as follows:
# A and B are playing each other
# If both A and B collaborate, 3 points each
# If A collaborates and B defects, A gets 0 points, B gets 5 points, and vice versa
# If both A and B defect, 1 point each
points = {
    ("C","C"): (3,3),
    ("C","D"): (0,5),
    ("D","C"): (5,0),
    ("D","D"): (1,1)
}

a_pts = 0
b_pts = 0
a_hist = []
b_hist = []

NUM_ROUNDS = 5000
ALLOWED_MOVES = ["C","D"]


for n in range(NUM_ROUNDS):
    a_move = A_STRAT(a_hist)
    b_move = B_STRAT(b_hist)

    if a_move not in ALLOWED_MOVES or b_move not in ALLOWED_MOVES:
        raise ValueError
    
    a_pts += points[a_move, b_move][0]
    b_pts += points[a_move, b_move][1]
    a_hist.append([a_move, b_move])
    b_hist.append([b_move, a_move])
    
print(a_pts, b_pts)