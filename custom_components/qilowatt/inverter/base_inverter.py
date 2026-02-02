# custom_components/qilowatt/inverter/base_inverter.py

from abc import ABC, abstractmethod


class BaseInverter(ABC):
    """Abstract base class for inverter implementations."""

    def __init__(self, hass, config_entry):
        self.hass = hass
        self.config_entry = config_entry

    @abstractmethod
    def get_energy_data(self):
        """Retrieve ENERGY data."""
        pass

    @abstractmethod
    def get_metrics_data(self):
        """Retrieve METRICS data."""
        pass

    @abstractmethod
    def is_data_ready(self) -> bool:
        """Check if all critical sensors have valid data.
        
        Returns True only when all required sensor values are available,
        ensuring we don't send incomplete data to the MQTT broker.
        """
        pass
