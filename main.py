from tests.frequency import frequency

if __name__ == "__main__":
    input = "1100100100001111110110101010001000100001011010001100001000110100110001001100011001100010100010111000"
    ones, zeros, s_n, s_obs, p_value = frequency( input )
    print(ones, zeros, s_n, s_obs, p_value)