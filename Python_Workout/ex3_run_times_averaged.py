def run_times():
    total_time = 0
    number_of_runs = 0

    while True:
        answer = input("Enter 10 km run time: ")

        if not answer:
            break

        number_of_runs += 1
        total_time += float(answer)

    average_time = total_time / number_of_runs

    print(f'Average of {average_time}, over {number_of_runs} runs')


run_times()
