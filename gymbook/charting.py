import matplotlib.pyplot as plt
import matplotlib.dates as mdates

def number_average_rep_weight_exercise(df, exercise):
    """
    
    """
    exercise_df = df[df['Exercise'] == exercise]
    
    # Create the plot
    plt.figure()

    plt.bar(exercise_df['Date'], exercise_df['Number Average Rep Weight'])
    plt.xticks(rotation='vertical')
    
    # https://matplotlib.org/3.1.1/gallery/text_labels_and_annotations/date.html
    years = mdates.YearLocator()   # every year
    months = mdates.MonthLocator()  # every month
    days = mdates.DayLocator() # every day

    ax = plt.gca()
    #set ticks every week
    ax.xaxis.set_major_locator(days)
    #set major ticks format
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%d %b')) # https://matplotlib.org/3.1.1/api/dates_api.html#matplotlib.dates.DateFormatter
    
    plt.show()