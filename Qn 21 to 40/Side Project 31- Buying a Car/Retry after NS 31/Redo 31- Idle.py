def nbMonths(startPriceOld, startPriceNew, savingperMonth, percentLossByMonth):
    money = startPriceOld
    time = 0 
    while money < startPriceNew:
        time = time + 1
        saved = savingperMonth * time
        percentLossByMonth = (percentLossByMonth + 0.5) if time%2 == 0 else percentLossByMonth
        startPriceNew = startPriceNew/100 * (100 - percentLossByMonth)
        startPriceOld = startPriceOld/100 * (100 - percentLossByMonth)
        money = startPriceOld + saved
    return [time, round(money - startPriceNew)]