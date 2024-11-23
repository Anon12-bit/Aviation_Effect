import hashlib
import random
import string

# Function to generate a random string of a given length
def generate_random_string(length):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

# Function to calculate differing bits between two hashes
def calculate_diff_bits(hash1, hash2):
    # Convert hashes to binary
    bin_hash1 = bin(int(hash1, 16))[2:].zfill(len(hash1) * 4)
    bin_hash2 = bin(int(hash2, 16))[2:].zfill(len(hash2) * 4)
    # Count differing bits
    return sum(b1 != b2 for b1, b2 in zip(bin_hash1, bin_hash2))

# Function to perform the Avalanche Effect test
def avalanche_effect_test(input_string, algorithm):
    # Modify one random character in the string
    random_index = random.randint(0, len(input_string) - 1)
    modified_string = (input_string[:random_index] + 
                       random.choice(string.ascii_letters + string.digits) + 
                       input_string[random_index + 1:])
    
    # Compute hashes
    original_hash = hashlib.new(algorithm, input_string.encode()).hexdigest()
    modified_hash = hashlib.new(algorithm, modified_string.encode()).hexdigest()
    
    # Compare bit differences
    diff_bits = calculate_diff_bits(original_hash, modified_hash)
    total_bits = len(original_hash) * 4  # Total bits in the hash
    return {
        "algorithm": algorithm.upper(),
        "input_string": input_string,
        "modified_string": modified_string,
        "original_hash": original_hash,
        "modified_hash": modified_hash,
        "differing_bits": diff_bits,
        "percentage_change": (diff_bits / total_bits) * 100
    }

# Main function to test Avalanche Effect with random strings
def run_avalanche_effect_tests():
    string_length = int(input("Enter the length of random strings: "))
    algorithms = ['md5', 'sha1', 'sha256']
    
    # Generate a random string
    random_string = generate_random_string(string_length)
    
    # Perform Avalanche Effect test for each algorithm
    results = [avalanche_effect_test(random_string, algo) for algo in algorithms]
    
    # Print results
    print("\nAvalanche Effect Test Results:")
    for result in results:
        print(f"\nAlgorithm: {result['algorithm']}")
        print(f"Input String: {result['input_string']}")
        print(f"Modified String: {result['modified_string']}")
        print(f"Original Hash: {result['original_hash']}")
        print(f"Modified Hash: {result['modified_hash']}")
        print(f"Differing Bits: {result['differing_bits']}")
        print(f"Percentage Change: {result['percentage_change']:.2f}%")

# Run the tests
run_avalanche_effect_tests()
