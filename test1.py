import talib
import bt 
import datetime
import matplotlib
matplotlib.use('TkAgg', force=True)
import matplotlib.pyplot as plt
import pandas as pd

today = datetime.datetime.now()

end1 = today.strftime("%m-%d-%Y")
start1 = today - datetime.timedelta(weeks=24)

beginning = start1.strftime("%m-%d-%Y")

# import data
test1 = bt.get(tickers=['chgg', 'amc'], start=beginning, end=today)
print(test1)

# plot data
# fig, (ax1, ax2) = plt.subplots(2)
# ax1.plot(test1['amc'])
# ax2.plot(test1['chgg'])
# plt.show()

# create signals
test1['amc_ema7'] = talib.EMA(test1['amc'], timeperiod=7)
test1['amc_ema14'] = talib.EMA(test1['amc'], timeperiod=14)

test1['amc_rsi7'] = talib.RSI(test1['amc'], timeperiod=5)

test1['chgg_ema7'] = talib.EMA(test1['chgg'], timeperiod=7)
test1['chgg_ema14'] = talib.EMA(test1['chgg'], timeperiod=14)

test1['chgg_rsi7'] = talib.RSI(test1['chgg'], timeperiod=5)

fig, axs = plt.subplots(2, 2)
axs[0, 0].set_title('amc ema')
axs[0, 0].plot(test1['amc'])
axs[0, 0].plot(test1['amc_ema7'])
axs[0, 0].plot(test1['amc_ema14'])

axs[0, 1].set_title('chgg ema')
axs[0, 1].plot(test1['chgg'])
axs[0, 1].plot(test1['chgg_ema7'])
axs[0, 1].plot(test1['chgg_ema14'])

axs[1, 0].set_title('Amc')
axs[1, 0].plot(test1['amc_rsi7'])

axs[1, 1].set_title('Chgg')
axs[1, 1].plot(test1['chgg_rsi7'])

# create strategies
data = pd.DataFrame()
ema = pd.DataFrame()
data['Close'] = test1['amc']
ema['Close'] = test1['amc_ema7']
# strat 1 - EMA signal
amc_strat1 = bt.Strategy('AboveEMA',
                         [bt.algos.SelectWhere(data > ema),
                         bt.algos.WeighEqually(),
                         bt.algos.Rebalance()]
                         )

bt1 = bt.Backtest(amc_strat1, ema)
result1 = bt.run(bt1)
result1.plot()
plt.show()
# strat 2 - 

# strat 3 - 

# performance evaluation


