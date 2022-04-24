import random
import sys

def run_trial(switch_doors, ndoors=3):
    """
    Run a single trial of the Monty Hall problem, with or without switching
    after the gameshow host reveals a goat behind one of the unchosen doors.
    (switch_doors is True or False). The car is behind door number 1 and the
    gameshow host knows that.

    """

    # Pick a random door out of the ndoors available
    chosen_door = random.randint(1, ndoors)
    if switch_doors:
        # Reveal a goat
        revealed_door = 3 if chosen_door==2 else 2
        # Make the switch by choosing any other door than the initially-
        # selected one and the one just opened to reveal a goat. 
        available_doors = [dnum for dnum in range(1,ndoors+1)
                                if dnum not in (chosen_door, revealed_door)]
        chosen_door = random.choice(available_doors)

    # You win if you picked door number 1
    return chosen_door == 1

def run_trials(ntrials, switch_doors, ndoors=3):
    """
    Run ntrials iterations of the Monty Hall problem with ndoors doors, with
    and without switching (switch_doors = True or False). Returns the number
    of trials which resulted in winning the car by picking door number 1.

    """

    nwins = 0
    for i in range(ntrials):
        if run_trial(switch_doors, ndoors):
            nwins += 1
    return nwins

ndoors, ntrials = 3, 10000 
if len(sys.argv) > 1:
    ndoors, ntrials = sys.argv[1].split(',')
nwins_without_switch = run_trials(int(ntrials), False, int(ndoors))
nwins_with_switch = run_trials(int(ntrials), True, int(ndoors))

print(f'Monty Hall Problem with {int(ndoors)} doors for {int(ntrials)} trials')
print('Proportion of wins without switching: {:.4f}'
            .format(nwins_without_switch/int(ntrials)))
print('Proportion of wins with switching: {:.4f}'
            .format(nwins_with_switch/int(ntrials)))