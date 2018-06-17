import matplotlib.pylab as plt


def plot_function(x_data, x_pred, y_data, y_pred):
    """Plot real and predicted data on the one graph.

    Args:
        x (ndarray).
        y_data (ndarray): real data.
        y_pred (ndarray): predicted data.

    """
    plt.figure(figsize=(10, 6))
    plt.plot(x_data, y_data, '-', color = 'b', label='actual data')
    plt.plot(x_pred, y_pred, '--', color = 'g', label='predicted data')
    plt.legend(loc='best')
    plt.show()


def word_amount(sentence):
    """Count amount of word in sentence.

    Args:
        sentence (str): string sentence.

    Returns
    --------
        amount (dict).

    """
    amount = dict()
    for word in sentence:
        if word in amount.keys():
            amount[word] += 1
        else:
            amount[word] = 1
    return amount