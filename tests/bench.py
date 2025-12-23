import sys, time, random
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))
import main.main, answers.moderate_alphabetical_main, answers.expert_bin_main, answers.advanced_length_main, answers.naive_main, answers.ultimate_set_main


NUM_SAMPLES = 5

SAMPLE_SIZE = 5000

with open("src/dictionary.txt", "r") as r:
    all_words = r.readlines()

all_samples = [random.sample(all_words, SAMPLE_SIZE) for x in range(NUM_SAMPLES)]

for i in range(len(all_words)):
    all_words[i] = all_words[i].strip()


def bench(name: str, method) -> float:
    
    averages = []
    print(f"- - - - - - - - - -\n{name}:\n")
    for sample in all_samples:
        start_time = time.time()
        for w in all_words:
            assert method(w)
        end_time = time.time()
        print(f"  {i}. {start_time} -> {end_time} == {end_time - start_time}")
        averages.append(end_time - start_time)
    
    print(f"  Overall: {sum(averages) / NUM_SAMPLES}")
    return sum(averages) / NUM_SAMPLES

bench("Your Version", main.main.is_word_valid)
bench("Set Based Search", answers.ultimate_set_main.is_word_valid)
bench("Binary Search By Length", answers.advanced_length_main.is_word_valid)
bench("Binary Search", answers.moderate_alphabetical_main.is_word_valid)
bench("Binary File", answers.expert_bin_main.is_word_valid)
bench("Naive Approach (Will take a long time)", answers.naive_main.is_word_valid)