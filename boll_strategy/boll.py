# ���ܱ��ογ����� ���ογ���Ҫ����ô���첢��д���� �����ʾ��������bollָ��Ϊ��  �������rsi\atrָ��
# �����û�йۿ� ���ƿ�ܽ��� ָ����� ��������Ƶ������ ���ע΢�Ź��ںš�ǧǧ���������硱  ΢�Ź��ںź�github������ṩ���ογ�Դ��
# ϲ�������� ������ ��ӭ�������ǵ���������΢������Ⱥ
# ��ʾ�����ογ���Ҫ����ô��д���� �´ογ��ٽ��ܻز�  
# BOLL����
def StrategyBoll(self):
	# ��ӡ�����Կ������
	kd, kk, pd, pk = self.kd, self.kk, self.pd, self.pk
	# ׼���ò������������
	upper = self.upper
	middle = self.middle
	lower = self.lower
	rsi = self.rsi6
	atr = self.atr
	trend_cur = upper[-2] - lower[-2]
	trend_pre = upper[-3] - lower[-3]
	# �����߼�  
	# ��������Խ���ԭ�� �Ͽ��� ��ƽ�� ���ƹ��Ƚ��� ͬʱ���ⱻ�����
	# ��ȡ��еķ�����1���࿴ͼ��2����������Ⱥ���� 
	# �������� �������󣨲��������� �������ϣ��������ƣ� ���ⳬ��ʱ�볡 �������������ƿ���������
	if upper[-2] > upper[-3] and middle[-2] > middle[-3] and lower[-2] < lower[-3]\
			and rsi[-2] < 70 and rsi[-2] > 50 and rsi[-2] > rsi[-3] and rsi[-1] < 80 and rsi[-1] > rsi[-2]\
			and atr[-2] > atr[-3] and trend_cur > trend_pre:
		self.kd += self.one_hand
		self.pk += self.one_hand
		if atr[-1] > atr[-2] and rsi[-1] < 60 and rsi[-1] > 50:
			self.kd += self.one_hand
	# �������� �������󣨲��������� �������£��������ƣ� ���ⳬ��ʱ�볡 �������������ƿ���������
	if upper[-2] > upper[-3] and middle[-2] < middle[-3] and lower[-2] < lower[-3]\
			and rsi[-2] > 30 and rsi[-2] < 50 and rsi[-2] < rsi[-3] and rsi[-1] > 20 and rsi[-1] < rsi[-2]\
			and atr[-2] > atr[-3] and trend_cur > trend_pre:
		self.kk += self.one_hand
		self.pd += self.one_hand
		if atr[-1] > atr[-2] and rsi[-1] > 40 and rsi[-1] < 50:
			self.kk += self.one_hand
	# ƽ������ ��������С �۸�ع����
	if upper[-2] < upper[-3] or lower[-2] > lower[-3]:
		if trend_cur < trend_pre and middle[-2] > middle[-3]:
			self.pk += self.one_hand
		if trend_cur < trend_pre and middle[-2] < middle[-3]:
			self.pd += self.one_hand
	self.log.info('���ԣ� BOLL  �źţ� kd:%d  kk:%d  pd:%d  pk:%d'%(self.kd - kd, self.kk- kk, self.pd - pd, self.pk - pk))