# -*- coding: utf-8 -*-
#jyoshida-sci 2015/08/31
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import fsolve


class RangeEnergy:
    #constants
    Mp = 938.272#proton mass
    LMp = np.log(Mp)#log(proton mass)
    D0 = 3.815#density of standard emulsion
    r = 0.884#parameter for E07 emulsion, default_r=1.0

    #def __init__(self):


    #from Nkzw-san's Fortran-code
    #This function returns range in standard emulsion in micron units
    #@param input Mass[MeV] of a particle
    #@param input KE[MeV] of a particle
    def RangeInStandardEmulsionNk(self, Mass, KE):
        KEM = KE / Mass
        LKEM = np.log10(KEM)

        if(KEM < 0.0001):
            return 479.210 * pow(KEM,0.675899)
        else:
            Rs = 6.05595
            Rs +=  1.38639 * LKEM
            Rs += -0.302838 * LKEM ** 2
            Rs += -0.0602134 * LKEM ** 3
            Rs +=  0.0359347 * LKEM ** 4
            Rs +=  0.0195023 * LKEM ** 5
            Rs +=  0.00348314 * LKEM ** 6
            Rs +=  0.000185264 * LKEM ** 7
            return 10.0 ** Rs


    #Mishina's fitting 2014
    #This function returns KE in standard emulsion in MeV units
    #@param input LnRange_mm
    # fitted by Mishina
    def ProtonKEfromRangeInStandardEmulsion_part1(self, LnRange_mm):
        LR = LnRange_mm
        LK = -2.288460778
        LK+= +1.382747508 * LR
        LK+= -0.439300692 * LR ** 2
        LK+= +0.162697682 * LR ** 3
        LK+= -0.037735480 * LR ** 4
        LK+= +0.005152047 * LR ** 5
        LK+= -0.000373872 * LR ** 6
        LK+= +0.000010917 * LR ** 7
        LnKE_MeV = LK
        return LnKE_MeV

    # fitted by Mishina
    def ProtonKEfromRangeInStandardEmulsion_part2(self, LnRange_mm):
        LR = LnRange_mm
        LK = 12.499454326
        LK+= -12.637449190 * LR
        LK+= +5.296813187 * LR ** 2
        LK+= -1.163641812 * LR ** 3
        LK+= +0.151898030 * LR ** 4
        LK+= -0.011803694 * LR ** 5
        LK+= +0.000505820 * LR ** 6
        LK+= -0.000009219 * LR ** 7
        LnKE_MeV = LK
        return LnKE_MeV

    # fitted by Mishina
    def ProtonKEfromRangeInStandardEmulsion_part3(self, LnRange_mm):
        LR = LnRange_mm
        LK = -0.52629642
        LK+= +0.31555326 * LR
        LK+= +0.021856192 * LR ** 2
        LK+= +0.0012217823 * LR ** 3
        LK+= -0.00026892371 * LR ** 4
        LK+= +0.00001057489 * LR ** 5
        LnKE_MeV = LK
        return LnKE_MeV


    # scipy.optimize.fsolveの返り値がnp.ndarrayなので、solution[0]として実数にしている。
    def RangeInStandardEmulsion(self, Mass, KE):
        if KE <= 0.0:
            return 0.0
        KEM = KE / Mass
        MKEM = np.log(KE * self.Mp / Mass)
        Rs = 0
        if(KEM < 0.0001):
            Rs = 479.210 * pow(KEM,0.675899)
        elif (MKEM < 1.930606146327):
            KEfunc = lambda LnRange_mm : self.ProtonKEfromRangeInStandardEmulsion_part1(LnRange_mm) - MKEM
            initial_guess = 3.0
            solution = fsolve(KEfunc, initial_guess)
            Rs = np.exp(solution[0])
        elif (MKEM < 4.405):
            KEfunc = lambda LnRange_mm : self.ProtonKEfromRangeInStandardEmulsion_part2(LnRange_mm) - MKEM
            initial_guess = 6.0
            solution = fsolve(KEfunc, initial_guess)
            Rs = np.exp(solution[0])
        else:
            KEfunc = lambda LnRange_mm : self.ProtonKEfromRangeInStandardEmulsion_part3(LnRange_mm) - MKEM
            initial_guess = 10.0
            solution = fsolve(KEfunc, initial_guess)
            Rs = np.exp(solution[0])
        return Rs


    #Mishina's original function
    def FunctionRs(self, KE, Mass):
        KEM = KE / Mass
        MKEM = np.log(KE * self.Mp / Mass)

        dd = 0.00001#;//step for italation

        if(KEM < 0.0001):
            Rs = 479.210 * pow(KEM,0.675899)

        elif (MKEM < 1.930606146327):
            d0 = 3.0000
            y0 = self.Rs_function1(d0)
            while abs(MKEM - y0) > 0.00001:
                d0 = (d0 + dd) if (MKEM > y0) else (d0 - dd)
                y0 = self.Rs_function1(d0)
            Rs = np.exp(d0)

        elif (MKEM < 4.405):
            d0 = 6.0000
            y0 = self.Rs_function2(d0)
            while abs(MKEM - y0) > 0.00001:
                d0 = (d0 + dd) if (MKEM > y0) else (d0 - dd)
                y0 = self.Rs_function2(d0)
            Rs = np.exp(d0)

        else:
            d0 = 10.0000
            y0 = self.Rs_function3(d0)
            while abs(MKEM - y0) > 0.00001:
                d0 = (d0 + dd) if (MKEM > y0) else (d0 - dd)
                y0 = self.Rs_function3(d0)
            Rs = np.exp(d0)

        return Rs


    #RsRwRatio fitted by Dr.Tovee and Dr.Gajewski
    def FunctionRsRwRatio(self, Rs):
        LRs = np.log(Rs)
        rate = -0.107714711
        rate += -0.332543998 * LRs
        rate += +0.141029694 * LRs ** 2
        rate += -0.044679440 * LRs ** 3
        rate += +0.008162611 * LRs ** 4
        rate += -0.000830409 * LRs ** 5
        rate += +0.000044038 * LRs ** 6
        rate += -0.000000951 * LRs ** 7
        return  np.exp(rate)


    #Cz fitted by Mishina
    def FunctionCz(self, Z, beta):
        if(Z == 1):
            return 0.0
        FX = 137.0 * beta / Z

        if FX <= 0.5:# //regionI: a*FX^b
            return  0.168550736771407 * pow(FX,1.90707106569386)
        elif FX <= 2.51:# regionII: polinominal7
            val = 0.002624371
            val += -0.081622520 * FX
            val += +0.643381535 * FX ** 2
            val += -0.903648583 * FX ** 3
            val += +0.697505012 * FX ** 4
            val += -0.302935572 * FX ** 5
            val += +0.067662990 * FX ** 6
            val += -0.006004180 * FX ** 7
            return val
        else:# regionIII: constant
            return 0.217598079611354


    #Energy->Range calculation
    def RangeFromKE(self, Mass, KE, Z, densityEM):
        if(KE <= 0.0):
            return 0.0

        #range as proton in standard emulsion
        Rs = self.RangeInStandardEmulsion(Mass, KE)#Mishina's fitting function
        #Rs = self.RangeInStandardEmulsionNk(Mass, KE)#Nakazawa-san's fitting function

        #correction for range
        ratio = self.FunctionRsRwRatio(Rs)# Rs/Rw ratio
        #F = densityEM / self.D0 + ((self.r * (self.D0 - densityEM)) / (self.r * self.D0 - 1.0)) * ratio #factor for range
        F = (self.r*densityEM-1)/(self.r*self.D0-1) + ((self.r * (self.D0 - densityEM)) / (self.r * self.D0 - 1.0)) * ratio #factor for range
        Rp = Rs / F#range as proton in this emulsion

        #calculating Cz
        E = Mass + KE #total energy
        P = np.sqrt(E * E - Mass * Mass) #momentum norm
        beta = P / E #beta of particle
        Cz = self.FunctionCz(Z, beta)

        #correction factors
        CPS = 1
        CPM = 1
        CF = 1

        #Range
        R1 = CPS * (Mass / self.Mp) / (Z * Z) * Rp
        R2 = CPM * (Mass / self.Mp) * pow(Z,2.0 / 3.0) * Cz #R_ext
        R = (R1 + R2) / CF
        return R


    #This is the inverse-function of RangeFromKineticEnergy
    # scipy.optimize.fsolveの返り値がnp.ndarrayなので、solution[0]として実数にしている。
    def KEfromRange(self, Mass, Range, Z, densityEM):
        if Range <= 0.0:
            return 0.0

        Rfunc = lambda KE : self.RangeFromKE(Mass,KE,Z,densityEM) - Range
        initial_guess = 1.0#any positive number
        solution = fsolve(Rfunc, initial_guess)
        return solution[0]


    def RangeStragglingFromKE(self, Mass, KE, Z, densityEM):
        KEM = KE / Mass
        M = Mass / self.Mp
        KEoverM = KE / M
        factorRangeStraggling = 0.0

        LogKEoverM = np.log10(KEoverM)
        if LogKEoverM < np.log10(2000 / M):
            factorRangeStraggling = 1.0164402329033 * pow(10.0, 0.30754491034543 - 0.110592840462518 * LogKEoverM) / 100
        else:
            factorRangeStraggling = pow(10.0, -0.461423281494685 + 0.124489776442783 * LogKEoverM) / 100

        dRp = 0
        if KEM < 0.0001:
            dRp = 479.210 * pow(KEoverM / self.Mp, 0.675899)
        else:
            #多項式フィットしたものby Mishina
            val = 1.147272863
            val +=  1.481654835 * LogKEoverM
            val +=  0.156395018 * LogKEoverM ** 2
            val += -0.078039243 * LogKEoverM ** 3
            val +=  0.065765281 * LogKEoverM ** 4
            val += -0.030414179 * LogKEoverM ** 5
            val +=  0.005482754 * LogKEoverM ** 6
            val += -0.000336044 * LogKEoverM ** 7
            dRp = pow(10.0, val)

        return np.sqrt(M) / (Z * Z) * dRp * factorRangeStraggling


    def RangeStragglingFromRange(self, Mass, Range, Z, densityEM):
        KE = self.KEfromRange(Mass, Range, Z, densityEM)
        return self.RangeStragglingFromKE(Mass, KE, Z, densityEM)


    ######for Display
    #1
    def DisplayRangeInStandardEmulsionNk(self,Mass):
        KEs = []
        Ranges = []
        for KE in range(100):
            KEs.append(KE)
            Ranges.append(self.RangeInStandardEmulsionNk(Mass, KE))

        plt.plot(KEs, Ranges)
        plt.xlabel("KE")
        plt.ylabel("Range")
        plt.grid()
        plt.show()


    #2
    def DisplayProtonKEfromRangeInStandardEmulsion(self):
        Ranges = []
        LRs = []
        Rs1s = []
        Rs3s = []
        for Range in range(1,3000):
            Ranges.append(Range)
            LR = np.log(Range)
            LRs.append(LR)
            Rs1s.append(np.exp(re.ProtonKEfromRangeInStandardEmulsion_part1(LR)))
            Rs3s.append(np.exp(re.ProtonKEfromRangeInStandardEmulsion_part3(LR)))

        #2は定数項が+12でなので、ゼロ近傍でものすごいことになる
        Ranges2 = []
        LRs2 = []
        Rs2s = []
        for Range in range(10,3000):
            Ranges2.append(Range)
            LR = np.log(Range)
            LRs2.append(LR)
            Rs2s.append(np.exp(re.ProtonKEfromRangeInStandardEmulsion_part2(LR)))

        plt.plot(Ranges, Rs1s)
        plt.plot(Ranges2, Rs2s)
        plt.plot(Ranges, Rs3s)
        plt.xlabel("Range[mm]")
        plt.ylabel("KE")
        plt.grid()
        plt.show()


    #3
    def DisplayRangeInStandardEmulsion(self, Mass):
        KEs = []
        Ranges = []
        for KE in range(260):
            KEs.append(KE)
            Range = re.RangeInStandardEmulsion(Mass, KE)
            Ranges.append(Range / 10000)#in cm units
        plt.plot(KEs, Ranges)
        plt.xlabel("KE")
        plt.ylabel("RangeInStandardEmulsion [cm]")
        plt.grid()
        plt.show()

    #4----

    #5
    def DisplayFunctionRsRwRatio(self):
        Rss = []
        RsRws = []
        for Rs in range(500):
            Rss.append(Rs)
            RsRw = re.FunctionRsRwRatio(Rs)
            RsRws.append(RsRw)

        plt.plot(Rss, RsRws)
        plt.xlabel("Rs")
        plt.ylabel("RsRw")
        plt.grid()
        plt.show()


    #6
    def DisplayFunctionCz(self):
        czs = []
        betas = []
        for i in range(50):
            beta = i * 0.001
            betas.append(beta)
            czs.append(re.FunctionCz(2, beta))

        plt.plot(betas, czs)
        plt.xlabel("beta")
        plt.ylabel("Cz")
        plt.grid()
        plt.show()


    #7
    def DisplayRangeFromKE(self, Mass, Z, densityEM):
        KEs = []
        Ranges = []
        for KE in range(100):
            KEs.append(KE)
            Range = re.RangeFromKE(Mass, KE, Z, densityEM)
            Ranges.append(Range)

        plt.plot(KEs, Ranges)
        plt.xlabel("KE")
        plt.ylabel("range")
        plt.grid()
        plt.show()


    #8
    def DisplayKEfromRange(self, Mass, Z, densityEM):
        KEs = []
        Ranges = []
        for Range in range(500):
            Ranges.append(Range)
            KE = re.KEfromRange(Mass, Range, Z, densityEM)
            KEs.append(KE)

        plt.plot(Ranges, KEs)
        plt.xlabel("Range")
        plt.ylabel("KE")
        plt.grid()
        plt.show()


    # usage (ProtonKEfromRangeInStandardEmulsion_partX() are not called from users usually)
    def UsageOfProtonKEfromRangeInStandardEmulsions(self):
        myr_cm = 4.1 * 10 ** -1#[cm]
        myr_mm = myr_cm * 10
        myke = np.exp(re.ProtonKEfromRangeInStandardEmulsion_part1(np.log(myr_mm)))
        print('{1:.2f} MeV  {0:.2f}cm'.format(myr_cm,myke))

        myr_cm = 14.4 * 10 ** -1#[cm]
        myr_mm = myr_cm * 10
        myke = np.exp(re.ProtonKEfromRangeInStandardEmulsion_part1(np.log(myr_mm)))
        print('{1:.2f} MeV  {0:.2f}cm'.format(myr_cm,myke))

        myr_cm = 18.7 * 10 ** -1#[cm]
        myr_mm = myr_cm * 10
        myke = np.exp(re.ProtonKEfromRangeInStandardEmulsion_part1(np.log(myr_mm)))
        print('{1:.2f} MeV  {0:.2f}cm'.format(myr_cm,myke))


# for validation between data and this calculation
def ProtonRangeTable():
    energies = [0.1, 0.2, 0.3, 0.4, 0.6, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0]
    lambdas = [0.99, 1.78, 2.76, 3.91, 6.69, 13.92, 25.63, 39.98, 57.06, 76.7, 98.3, 122.3]
    Z = 1
    densityEM = 3.815
    print("Table in Nuclear Research Emulsion by Barkas p.435")
    print("----------------------------------")
    print("#proton_energy[MeV] emulsion_lambda[micron]")
    for i,e in enumerate(energies):
        print("{0} {1:.2f}".format(e, lambdas[i]))
    print("----------------------------------")
    print("")
    print("calculated values by this")
    print("----------------------------------")
    print("#tau[MeV]  calculated_lambda[micron]  diff[micron]")
    for i,e in enumerate(energies):
        calculated_lambda = re.RangeFromKE(re.Mp, e, Z, densityEM)
        print("{0}  ".format(e), end="")
        print("{0:.2f}  ".format(calculated_lambda), end="")
        print("{0:.2f}".format(calculated_lambda - lambdas[i]))
    print("----------------------------------")


def RangeStragglingTable():
    Z = 1
    densityEM = 3.815
    #tau = [1,2,5,10,20,50,100,200,500,1000,2000,5000,10000]
    taus = [1, 2, 5, 10, 20, 50, 100, 200]
    vals = [2.11, 1.94, 1.66, 1.53, 1.42, 1.29, 1.21, 1.13]
    print("Table in Nuclear Research Emulsion by Barkas p.455")
    print("----------------------------------")
    print("#tau[MeV] 100/M^(1/2)sigmaR/R [%]")
    for i,t in enumerate(taus):
        print("{0} {1:.2f}".format(t, vals[i]))
    print("----------------------------------")
    print("")
    print("calculated values by this")
    print("----------------------------------")
    print("#tau[MeV]  val_by_KE  val_by_range  diff")
    for i,t in enumerate(taus):
        R = re.RangeFromKE(re.Mp, t, Z, densityEM)
        sigmaR_from_KE = re.RangeStragglingFromKE(re.Mp, t, Z, densityEM)
        val_from_KE = 100.0 * np.sqrt(re.Mp / re.Mp) * sigmaR_from_KE / R
        sigmaR_from_range = re.RangeStragglingFromRange(re.Mp, R, Z, densityEM)
        val_from_range = 100.0 * np.sqrt(re.Mp / re.Mp) * sigmaR_from_range / R
        print("{0}  ".format(t), end="")
        print("{0:.2f}  ".format(val_from_KE), end="")
        print("{0:.2f}  ".format(val_from_range), end="")
        print("{0:.2f}".format(val_from_range - vals[i]))
    print("----------------------------------")



if __name__ == "__main__":

    re = RangeEnergy()
    # when you use this as external module,
    #import rangeenergy
    #re = rangeenergy.RangeEnergy()

    # display graphs
    # re.DisplayRangeInStandardEmulsionNk(re.Mp)
    # re.DisplayProtonKEfromRangeInStandardEmulsion()
    # re.DisplayRangeInStandardEmulsion(re.Mp)
    # re.DisplayFunctionRsRwRatio()
    # re.DisplayFunctionCz()
    # re.DisplayRangeFromKE(re.Mp, 1, re.D0)
    # re.DisplayKEfromRange(re.Mp, 1, re.D0)

    # usage: alpha from 212Po
    mass_alpha = 3727.379
    # print(re.RangeFromKE(mass_alpha, 8.785, 2, 3.815))# "47.96061"
    # print(re.KEfromRange(mass_alpha, 47.96061, 2, 3.815))# "8.785"

    # usage: KEfromRange
    # print(re.KEfromRange(938.272, 500.10, 1, 3.6))
    # print(re.KEfromRange(938.272, 1000.10, 1, 3.6))
    # print(re.KEfromRange(938.272, 1500.10, 1, 3.6))

    # usage: RangeStraggling
    # print("Proton range 5 MeV in standard emulsion:")
    # print("{0:.1f} +- {1:.1f} [micron]\n".format(
    #         re.RangeFromKE(re.Mp, 5, 1, 3.815),
    #         re.RangeStragglingFromKE(re.Mp, 5, 1, 3.815)
    #         ))

    # validation between data and this calculation
    # ProtonRangeTable()
    # RangeStragglingTable()

    print("{0:.1f} +- {1:.1f} [micron]\n"
          .format(re.RangeFromKE(mass_alpha, 8.785, 2, 3.544),
                  re.RangeStragglingFromRange(mass_alpha, 50.25, 2, 3.544)))
