import requests
import matplotlib.pyplot as plt
import ctypes
import os

# LeetCode GraphQL endpoint
url = "https://leetcode.com/graphql/"

# GraphQL query
query = """
  query getLeetCodeProfile($username: String!) {
    matchedUser(username: $username) {
      username
      submitStats: submitStatsGlobal {
        acSubmissionNum {
          difficulty
          count
          submissions
        }
      }
    }
  }
"""
# TODO: CHANGE THE USERNAME TO YOUR USERNAME !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# Variables for the query
variables = {
    "username": "jawadur"  # Replace with the username you want to query
}

# Function to fetch data from LeetCode
def get_leetcode_data():
    try:
        response = requests.post(
            url,
            headers={"Content-Type": "application/json"},
            json={"query": query, "variables": variables},
        )

        data = response.json()
        return data["data"]["matchedUser"]["submitStats"]["acSubmissionNum"]

    except Exception as e:
        print("Error:", e)
        return None  # Handle errors gracefully

# Fetch the data
result = get_leetcode_data()

if result:
    # Extract difficulties and counts
    difficulties = [item["difficulty"] for item in result]
    counts = [item["count"] for item in result]

    # Define colors for each difficulty
    colors = {
        "All": "blue",  # 🔵 All (Total)
        "Easy": "green",  # 🟢 Easy
        "Medium": "orange",  # 🟠 Medium
        "Hard": "red"  # 🔴 Hard
    }
    
    # Get corresponding colors
    bar_colors = [colors.get(difficulty, "gray") for difficulty in difficulties]

    # Set dark background theme
    plt.style.use("dark_background")

    # Create the bar chart
    plt.figure(figsize=(8, 5))
    bars = plt.bar(difficulties, counts, color=bar_colors)

    # Add numbers on top of each bar
    for bar in bars:
        height = bar.get_height()
        plt.text(bar.get_x() + bar.get_width() / 2, height, f"{height}", 
                 ha="center", va="bottom", fontsize=12, fontweight="bold", color="white")

    # Labels and title
    plt.xlabel("Difficulty Level", fontsize=12, color="white")
    plt.ylabel("Solved Problems", fontsize=12, color="white")
    plt.title(f"LeetCode Submissions for {variables['username']}", fontsize=14, color="white")
    plt.xticks(rotation=45, fontsize=10, color="white")
    plt.yticks(fontsize=10, color="white")
    plt.grid(axis="y", linestyle="--", alpha=0.4, color="gray")

    # Save the image
    image_filename = "leetcode_stats.png"
    plt.savefig(image_filename, dpi=300, bbox_inches="tight")
    print(f"Image saved as {image_filename}")

    # Change the windows background to this image
    image_path = os.path.abspath(image_filename)  # Get full path automatically
    SPI_SETDESKWALLPAPER = 20
    ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, image_path, 3)
    print("Wallpaper changed successfully.")
    
else:
    print("Failed to retrieve data.")
