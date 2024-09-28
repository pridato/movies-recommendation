import matplotlib.pyplot as plt


def plot_data(users, films, ratings):
    """
    Function to plot the data
    @param films: List[str] - list of films
    @param ratings: List[float] - list of ratings
    """
    plt.figure(figsize=(15, 8))

    bars = plt.bar(films, ratings, color="skyblue")

    # Displaying the film names on the x-axis and rotating them
    plt.xticks(rotation=45, ha="right")

    # Adding grid lines

    # Adding data labels on top of the bars
    for bar in bars:
        yval = bar.get_height()
        plt.text(
            bar.get_x() + bar.get_width() / 2,
            yval,
            round(yval, 2),
            ha="center",
            va="bottom",
        )

    plt.xlabel("Films")
    plt.ylabel("Rating")
    plt.title("Average rating per film by {} users".format(users))
    plt.show()
