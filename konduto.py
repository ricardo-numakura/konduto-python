class Konduto(object):
	""" <summary>
	 Konduto is an HTTP Client for connecting to Konduto's API.
	 </summary>
	"""
	def __init__(self, apiKey):
		self._VERSION = "1.0.9"
		self.___MessageHandler = None
		self._useProxy = False
		self.SetApiKey(apiKey)
		self._endpoint = Uri("https://api.konduto.com/v1/")

	def SetEndpoint(self, endpoint):
		""" <summary>
		 Konduto's API endpoint (default is https://api.konduto.com/v1/)
		 </summary>
		 <param name="endpoint"></param>
		"""
		self._endpoint = endpoint

	def SetApiKey(self, apiKey):
		""" <summary>
		 sets the merchant secret API key, which is required for Konduto's API authentication.
		 </summary>
		 <param name="apiKey"></param>
		"""
		if apiKey == None or apiKey.Length != 21:
			raise ArgumentOutOfRangeException("Illegal API Key: " + apiKey)
		self._apiKey = apiKey

	def Debug(self):
		""" <summary>
		 Helper method to debug requests made to Konduto's API.
		 </summary>
		 <returns>a String containing API Key, Konduto's API endpoint, request and response bodies.</returns>
		"""
		sb = StringBuilder()
		sb.Append(String.Format("API Key: {0}\n", self._apiKey))
		sb.Append(String.Format("Endpoint: {0}\n", self._endpoint.ToString()))
		if self._requestBody != None:
			sb.Append(String.Format("Request body: {0}\n", self._requestBody))
		if self._responseBody != None:
			sb.Append(String.Format("Response body: {0}\n", self._responseBody))
		return sb.ToString()

	def KondutoGetOrderUrl(self, orderId):
		""" <summary>
		 </summary>
		 <param name="orderId">the order identifier</param>
		 <returns>[GET] order URI (ENDPOINT/orders/orderId)</returns>
		"""
		return Uri(self._endpoint.ToString() + self.KondutoGetOrderSuffix(orderId))

	def KondutoGetOrderSuffix(self, orderId):
		""" <summary>
		 </summary>
		 <param name="orderId">the order identifier</param>
		 <returns>/orders/orderId</returns>
		"""
		return "orders/" + orderId

	def KondutoPostOrderUrl(self):
		""" <summary>
		 [POST] order URI (ENDPOI
