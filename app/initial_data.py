import logging
from decimal import Decimal
from sqlmodel import Session, select

from app.core.db import engine
from app.models.product import Product, Category

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def init_db(session: Session) -> None:
    # Check if products already exist
    statement = select(Product)
    result = session.exec(statement)
    first_product = result.first()
    
    if first_product:
        logger.info("Products already exist in the database. Skipping seeding.")
        return

    products_data = [
        # CPUs
        {
            "name": "AMD Ryzen 7 7800X3D",
            "slug": "amd-ryzen-7-7800x3d",
            "category": Category.CPU,
            "specs": {"socket": "AM5", "cores": 8, "base_clock": "4.2GHz", "tdp": 120, "integrated_graphics": True},
            "price": Decimal("449.00"),
            "stock": 10,
            "description": "The ultimate gaming processor with AMD 3D V-Cache technology."
        },
        {
            "name": "Intel Core i9-13900K",
            "slug": "intel-core-i9-13900k",
            "category": Category.CPU,
            "specs": {"socket": "LGA1700", "cores": 24, "base_clock": "3.0GHz", "tdp": 125, "integrated_graphics": True},
            "price": Decimal("589.00"),
            "stock": 10,
            "description": "24 cores (8 P-cores + 16 E-cores) and up to 5.8 GHz."
        },
        # Motherboards
        {
            "name": "ASUS ROG Strix B650-A",
            "slug": "asus-rog-strix-b650-a",
            "category": Category.MOTHERBOARD,
            "specs": {"socket": "AM5", "form_factor": "ATX", "ram_type": "DDR5", "max_ram": 128},
            "price": Decimal("279.99"),
            "stock": 10,
            "description": "Gaming WiFi 6E motherboard with robust power solution."
        },
        {
            "name": "MSI MPG Z790 Edge",
            "slug": "msi-mpg-z790-edge",
            "category": Category.MOTHERBOARD,
            "specs": {"socket": "LGA1700", "form_factor": "ATX", "ram_type": "DDR5", "max_ram": 128},
            "price": Decimal("369.99"),
            "stock": 10,
            "description": "Stylish silver white aesthetic with high performance."
        },
        # RAM
        {
            "name": "Corsair Vengeance 32GB (2x16GB) DDR5",
            "slug": "corsair-vengeance-32gb-ddr5",
            "category": Category.RAM,
            "specs": {"type": "DDR5", "speed": "6000MHz", "capacity": "32GB", "modules": 2},
            "price": Decimal("119.99"),
            "stock": 20,
            "description": "High-performance DDR5 memory for Intel and AMD."
        },
        # GPU
        {
            "name": "NVIDIA RTX 4080 Super",
            "slug": "nvidia-rtx-4080-super",
            "category": Category.GPU,
            "specs": {"vram": "16GB", "length_mm": 310, "recommended_watts": 750},
            "price": Decimal("999.00"),
            "stock": 5,
            "description": "Supercharged performance and efficiency for 4K gaming."
        },
        # Drones
        {
            "name": "DJI Mini 4 Pro",
            "slug": "dji-mini-4-pro",
            "category": Category.DRONE,
            "specs": {"flight_time": "34min", "range": "20km", "camera": "4K"},
            "price": Decimal("759.00"),
            "stock": 8,
            "description": "Mini camera drone with omnidirectional obstacle sensing."
        },
        # PSU
        {
            "name": "Corsair RM850x Shift",
            "slug": "corsair-rm850x-shift",
            "category": Category.PSU,
            "specs": {"watts": 850, "form_factor": "ATX", "modular": "Full", "certification": "80 Plus Gold"},
            "price": Decimal("149.99"),
            "stock": 15,
            "description": "High-performance ATX power supply with modular cables."
        },
        {
            "name": "EVGA 600 W1",
            "slug": "evga-600-w1",
            "category": Category.PSU,
            "specs": {"watts": 600, "form_factor": "ATX", "modular": "Non-Modular", "certification": "80 Plus White"},
            "price": Decimal("49.99"),
            "stock": 10,
            "description": "Compact ATX power supply with non-modular cables."
        },
        # CASE
        {
            "name": "Corsair Obsidian 500 RGB",
            "slug": "corsair-obsidian-500-rgb",
            "category": Category.CASE,
            "specs": {"form_factor": "ATX", "front_ports": 2, "rear_ports": 6, "side_ports": 2, "dimensions": "450x180x450mm"},
            "price": Decimal("149.99"),
            "stock": 15,
            "description": "High-performance ATX power supply with modular cables."
        },
        {
            "name": "NZXT H510",
            "slug": "nzxt-h510",
            "category": Category.CASE,
            "specs": {"form_factor": "ATX", "front_ports": 2, "rear_ports": 6, "side_ports": 2, "dimensions": "450x180x450mm"},
            "price": Decimal("149.99"),
            "stock": 15,
            "description": "High-performance ATX power supply with modular cables."
        },
        # STORAGE
        {
            "name": "Samsung 990 Pro 2TB",
            "slug": "samsung-990-pro-2tb",
            "category": Category.STORAGE,
            "specs": {"type": "M.2 NVMe", "capacity": "2TB", "read_speed": "7450 MB/s", "generation": "Gen4"},
            "price": Decimal("149.99"),
            "stock": 15,
            "description": "High-performance ATX power supply with modular cables."
        },
        {
            "name": "Kingston NV2 1TB",
            "slug": "kingston-nv2-1tb",
            "category": Category.STORAGE,
            "specs": {"type": "M.2 NVMe", "capacity": "1TB", "read_speed": "3500 MB/s", "generation": "Gen4"},
            "price": Decimal("149.99"),
            "stock": 15,
            "description": "High-performance ATX power supply with modular cables."
        }
    ]

    for product_data in products_data:
        product = Product(**product_data)
        session.add(product)
    
    session.commit()
    logger.info("Database seeded successfully!")

if __name__ == "__main__":
    with Session(engine) as session:
        init_db(session)
