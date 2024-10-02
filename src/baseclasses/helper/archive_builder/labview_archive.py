import numpy as np
from datetime import datetime

from nomad.units import ureg


def get_electrolyser_properties(metadata):
    # TODO decide if we need that for e.g. ids or other properties
    #properties = ElectrolyserProperties()
    user_name = metadata.get('Username')
    device = metadata.get('Device under test')
    #properties.comments = metadata.get('Comments')
    #return properties


def get_tdms_archive(data, entry_class):
    # TODO units like mln/minute (is mln normliter? then mln/minute might be slpm or standard liter per minute?)
    entry_class.time = np.array(data['READ_0_Time']) * ureg('s') if 'READ_0_Time' in data.columns else None
    entry_class.h2_flow = np.array(data['READ_H2_Flow']) * ureg('ml/minute') if 'READ_H2_Flow' in data.columns else None
    entry_class.o2_flow = np.array(data['READ_O2_Flow']) * ureg('ml/minute') if 'READ_O2_Flow' in data.columns else None
    entry_class.anode_in = np.array(data['READ_RTD0_A-in']) * ureg('°C') if 'READ_RTD0_A-in' in data.columns else None
    entry_class.cathode_in = np.array(data['READ_RTD1_C-in']) * ureg('°C') if 'READ_RTD1_C-in' in data.columns else None
    entry_class.anode_out = np.array(data['READ_RTD2_A-out']) * ureg('°C') if 'READ_RTD2_A-out' in data.columns else None
    entry_class.cathode_out = np.array(data['READ_RTD3_C-out']) * ureg('°C') if 'READ_RTD3_C-out' in data.columns else None
    entry_class.ambient = np.array(data['READ_RTD4_amb']) * ureg('°C') if 'READ_RTD4_amb' in data.columns else None
    entry_class.electrolyser_cell_anode = np.array(data['READ_RTD5_EC-A']) * ureg('°C') if 'READ_RTD5_EC-A' in data.columns else None
    entry_class.electrolyser_cell_cathode = np.array(data['READ_RTD6_EC-C']) * ureg('°C') if 'READ_RTD6_EC-C' in data.columns else None
    timestamp_array = np.array(data['READ_Timestamp']) if 'READ_Timestamp' in data.columns else None
    entry_class.timestamp = [datetime.fromtimestamp(timestamp) for timestamp in timestamp_array]
