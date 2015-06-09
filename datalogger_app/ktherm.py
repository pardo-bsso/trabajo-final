VOL_OFFSET = 330

AMP_AV     = 54.16
AREF       = 3.3


Var_VtoT_K = [
    [0, 2.5173462e1, -1.1662878, -1.0833638, -8.9773540/1e1, -3.7342377/1e1, -8.6632643/1e2, -1.0450598/1e2, -5.1920577/1e4],
    [0, 2.508355e1, 7.860106/1e2, -2.503131/1e1, 8.315270/1e2, -1.228034/1e2, 9.804036/1e4, -4.413030/1e5, 1.057734/1e6, -1.052755/1e8],
    [-1.318058e2, 4.830222e1, -1.646031, 5.464731/1e2, -9.650715/1e4, 8.802193/1e6, -3.110810/1e8]
]

def K_VtoT(mV):
    value = 0

    if (mV >= -6.478 and mV < 0):
        value = Var_VtoT_K[0][8]

        for i in range(8,0,-1):
            value = mV * value + Var_VtoT_K[0][i-1]

    elif(mV >= 0 and mV < 20.644):
        value = Var_VtoT_K[1][9]

        for i in range(9,0,-1):
            value = mV * value + Var_VtoT_K[1][i-1]

    elif(mV >= 20.644 and mV <= 54.900):
        value = Var_VtoT_K[2][6]

        for i in range(6,0,-1):
            value = mV * value + Var_VtoT_K[2][i-1]

    return value
