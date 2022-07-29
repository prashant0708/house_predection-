from collections import namedtuple


DataIngenctionConfig = namedtuple("DataIngenctionConfig",
["dataset_download_url","tgz_download_dir","raw_data_dir","ingested_train_dir","ingested_test_dir"])

DataValidationConfig = namedtuple("DataValidationsConfig",["schema_file_path"])