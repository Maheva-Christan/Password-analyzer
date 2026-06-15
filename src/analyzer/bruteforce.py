
def crack_time_detailed(time_seconds):
    """To detailed the time given in seconds"""

    minute = 60
    hour = 3_600
    day = 86_400
    month = 2_592_000
    year = 31_536_000

    f_year = time_seconds // year
    f_seconds = time_seconds % year

    f_month = f_seconds // month
    f_seconds %= month

    f_day = f_seconds // day
    f_seconds %= day

    f_hour = f_seconds // hour
    f_seconds %= hour

    f_minute = f_seconds // minute
    f_seconds %= minute
    
    return f"{int(f_year)} Year {int(f_month)} month {int(f_day)} Day {int(f_hour)} h {int(f_minute)} min {f_seconds:.3f} s"


def estimate_bruteforce(analysis):
    """To estimate the time to crack the password"""

    penalised_combination = analysis["penalised_combination"]
    real_combination = analysis["real_combination"]

    penalised_average_attempts = penalised_combination / 2
    real_average_attempts = real_combination / 2

    # These values can be different as the algorithm used to crack the password
    online_APS = 10
    weak_server_APS = 500
    modern_GPU_APS = 40_000_000_000
    cluster_GPU_APS = 40_000_000_000_000
    standard_offline_APS = 50_000

    print("\nEstimated bruteforce time:")
    if analysis["in_wordlist"]:

        crack_time = (len(analysis["words"]) / 2) / standard_offline_APS

        print(f"\t- Using this wordlist, your password can be cracked with:")
        print(f"\t   {crack_time_detailed(crack_time)}")

    
    print(f"\n\t- Website bruteforce attack:")
    print(f"\t   + With penalisation: {crack_time_detailed(penalised_average_attempts / online_APS)}")
    print(f"\t   + Without penalisation: {crack_time_detailed(real_average_attempts / online_APS)}")

    print(f"\n\t- Weak server attack:")
    print(f"\t   + With penalisation: {crack_time_detailed(penalised_average_attempts / weak_server_APS)}")
    print(f"\t   + Without penalisation: {crack_time_detailed(real_average_attempts / weak_server_APS)}")

    print(f"\n\t- Modern GPU attack (offline):")
    print(f"\t   + With penalisation: {crack_time_detailed(penalised_average_attempts / modern_GPU_APS)}")
    print(f"\t   + Without penalisation: {crack_time_detailed(real_average_attempts / modern_GPU_APS)}")
    
    print(f"\n\t- Cluster GPU attack (offline):")
    print(f"\t   + With penalisation: {crack_time_detailed(penalised_average_attempts / cluster_GPU_APS)}")
    print(f"\t   + Without penalisation: {crack_time_detailed(real_average_attempts / cluster_GPU_APS)}")

