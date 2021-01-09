class DeviceBase:
    uuid = None
    gsm_imei = None
    gsm_msisdn = None
    hw_version = None
    sw_version = None

    operation_mode = None
    disaster_time = None
    disaster_warning = None
    expected_primary_layer_failure = None
    expected_primary_layer_failure_till = None
    location_update_at = 10

    def __init__(self, uuid, gsm_imei, gsm_msisdn):
        self.uuid = uuid
        self.gsm_imei = gsm_imei
        self.gsm_msisdn = gsm_msisdn
