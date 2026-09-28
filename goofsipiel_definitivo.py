import sys
import random
import bisect

def read_line():
    return sys.stdin.readline().strip()
    
def greedy_pick(our_rem, opp_sorted, cur_pot):
    m = len(opp_sorted)
    best_c = None
    best_v = -float('inf')
    for cc in our_rem:
        left = bisect.bisect_left(opp_sorted, cc)
        right = m - bisect.bisect_right(opp_sorted, cc)
        v = (left - right) /m *cur_pot - cc
        if v > best_v:
            best_v = v
            best_c = cc
    return best_c
    
def evaluate_bid(c, our_cards, opp_cards, pot, future_prizes, know, num_sims):
    base_our = set(our_cards)
    base_our.discard(c)
    base_opp = set(opp_cards)
    
    total = 0.0
    for _ in range(num_sims):
        our_rem = set(base_our)
        opp_rem = set(base_opp)
        our_s =0
        opp_s = 0
        carry = 0
        
        if opp_rem:
            opp_bid = random.choice(tuple(opp_rem))
            opp_rem.discard(opp_bid)
        else:
            opp_bid = 0
            
        if c > opp_bid:
            our_s += pot
        elif c < opp_bid:
            opp_s += pot
        else:
            carry = pot
            
        future = list(future_prizes)
        if not know:
            random.shuffle(future)
            
        for prize in future:
                if not our_rem or not opp_rem:
                    break
                cur_pot = carry + prize
                opp_sorted = sorted(opp_rem)
                pick = greedy_pick(our_rem, opp_sorted, cur_pot)
                our_rem.discard(pick)
                ob = random.choice(tuple(opp_rem))
                opp_rem.discard(ob)
                
                if pick > ob:
                    our_s += cur_pot
                    carry = 0
                elif pick < ob:
                    opp_s += cur_pot
                    carry = 0
                else:
                    carry = cur_pot
        total += our_s - opp_s
        
    return total / num_sims
    
def choose_bid(our_cards, opp_cards, pot, remaining, know):
    n_our = len(our_cards)
    if n_our >= 20:
        sims = 8
    elif n_our >= 12:
        sims = 15
    elif n_our >= 6:
        sims = 30
    else:
        sims = 60
    
    best_bid = min(our_cards)
    best_score = -float('inf')
    
    for c in sorted(our_cards):
        score = evaluate_bid(c, our_cards, opp_cards, pot, remaining, know, sims)
        score -= c * 1e-6
        if score > best_score:
            best_score =score
            best_bid = c
            
    return best_bid
    

def main():
    try:
        line = read_line()
        while not line:
            line = read_line()
        parts = line.split()
        N = int(parts[1])
        know = int(parts[2]) == 1
        
        prize = []
        while len(prize) < N:
            line = read_line()
            if not line:
                continue
            p = line.split()
            if p and p[0] == "PRIZES":
                prize.extend(int(x) for x in p[1:])
        prize = prize [:N]
        
        our_cards = set(range(1, N + 1))
        opp_cards = set(range(1, N + 1))    
        remaining = list(prize)
        
        while True:
            line = read_line()
            if not line:
                continue
            parts = line.split()
            cmd = parts[0]
            
            if cmd == "GAME_END":
                break
            
            if cmd == "ROUND":
                prize = int(parts[1])
                pot = int(parts[2])
                
                if prize in remaining:
                    remaining.remove(prize)
                    
                bid = choose_bid(our_cards, opp_cards, pot, remaining, know)
                print(f"BID {bid}")
                sys.stdout.flush()
                our_cards.discard(bid)
            
            elif cmd == "RESULT":
                try:
                    opp_bid = int(parts[1])
                    opp_cards.discard(opp_bid)
                except (IndexError, ValueError):
                    pass
    
    except Execption as e:
        print(f"ERROR: {e}", file=sys.stderr)
        sys.exit(0)

if __name__ == "__main__":
    main()