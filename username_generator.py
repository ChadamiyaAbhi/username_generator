import random
import string

class UsernameGenerator:
    def __init__(self):
        # Lists of adjectives and nouns for username generation
        self.adjectives = [
            'Cool', 'Happy', 'Brave', 'Swift', 'Clever', 'Mystic', 'Wild', 'Gentle',
            'Fierce', 'Bright', 'Dark', 'Lucky', 'Magic', 'Royal', 'Silent', 'Wise'
        ]
        self.nouns = [
            'Tiger', 'Dragon', 'Phoenix', 'Wolf', 'Eagle', 'Lion', 'Panther', 'Falcon',
            'Hawk', 'Bear', 'Fox', 'Raven', 'Storm', 'Shadow', 'Blade', 'Spirit'
        ]
        self.special_chars = '!@#$%^&*'

    def generate_username(self, include_numbers=True, include_special_chars=False, min_length=8, max_length=15):
        # Randomly select an adjective and noun
        adjective = random.choice(self.adjectives)
        noun = random.choice(self.nouns)
        
        # Combine adjective and noun
        username = adjective + noun
        
        # Add numbers if requested
        if include_numbers:
            num_digits = random.randint(1, 3)
            username += ''.join(random.choices(string.digits, k=num_digits))
        
        # Add special characters if requested
        if include_special_chars:
            username += random.choice(self.special_chars)
        
        # Ensure username meets length requirements
        while len(username) < min_length:
            username += random.choice(string.digits)
        
        # Trim if too long
        if len(username) > max_length:
            username = username[:max_length]
        
        return username

    def save_usernames(self, usernames, filename='generated_usernames.txt'):
        try:
            with open(filename, 'a') as file:
                for username in usernames:
                    file.write(username + '\n')
            print(f"Usernames saved to {filename}")
        except Exception as e:
            print(f"Error saving usernames: {e}")

def main():
    generator = UsernameGenerator()
    
    print("Welcome to the Random Username Generator!")
    print("----------------------------------------")
    
    while True:
        try:
            num_usernames = int(input("How many usernames would you like to generate? (1-10): "))
            if num_usernames < 1 or num_usernames > 10:
                print("Please enter a number between 1 and 10.")
                continue
                
            include_numbers = input("Include numbers? (y/n): ").lower() == 'y'
            include_special_chars = input("Include special characters? (y/n): ").lower() == 'y'
            
            min_length = int(input("Minimum username length (8-15): "))
            max_length = int(input("Maximum username length (8-20): "))
            
            if min_length < 8 or max_length > 20 or min_length > max_length:
                print("Invalid length parameters. Using default values (8-15).")
                min_length, max_length = 8, 15
            
            # Generate usernames
            usernames = []
            for _ in range(num_usernames):
                username = generator.generate_username(
                    include_numbers=include_numbers,
                    include_special_chars=include_special_chars,
                    min_length=min_length,
                    max_length=max_length
                )
                usernames.append(username)
                print(f"Generated username: {username}")
            
            # Ask if user wants to save the usernames
            save = input("Would you like to save these usernames? (y/n): ").lower() == 'y'
            if save:
                generator.save_usernames(usernames)
            
            # Ask if user wants to generate more usernames
            again = input("Would you like to generate more usernames? (y/n): ").lower() == 'y'
            if not again:
                print("Thank you for using the Random Username Generator!")
                break
                
        except ValueError:
            print("Please enter valid numbers.")
        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    main() 