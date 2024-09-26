# ほとんどのコードは mikey_nodes のものを使っています
# https://github.com/bash-j/mikey_nodes

import os
import json
import hashlib
import folder_paths
import comfy.sd


def calculate_file_hash(file_path):
    # open the file in binary mode
    with open(file_path, 'rb') as f:
        # read the file in chunks to avoid loading the whole file into memory
        chunk_size = 4096
        hash_object = hashlib.sha256()
        while True:
            chunk = f.read(chunk_size)
            if not chunk:
                break
            hash_object.update(chunk)
    # return the hexadecimal representation of the hash
    return hash_object.hexdigest()

def get_cached_file_hashes():
    # load the cached file hashes from the JSON file
    cache_file_path = os.path.join(folder_paths.base_path, 'file_hashes.json')
    if os.path.exists(cache_file_path):
        with open(cache_file_path, 'r') as f:
            return json.load(f)
    else:
        return {}

def cache_file_hash(file_path, file_hash):
    # update the cached file hashes dictionary and save to the JSON file
    cache_file_path = os.path.join(folder_paths.base_path, 'file_hashes.json')
    cached_file_hashes = get_cached_file_hashes()
    cached_file_hashes[os.path.basename(file_path)] = file_hash
    with open(cache_file_path, 'w') as f:
        json.dump(cached_file_hashes, f)

def get_file_hash(file_path):
    # check if the file hash is already cached
    # replace \ with / in file_path
    file_path = file_path.replace('\\', '/')
    cached_file_hashes = get_cached_file_hashes()
    file_name = os.path.basename(file_path)
    if file_name in cached_file_hashes:
        return cached_file_hashes[file_name]
    else:
        # calculate the file hash and cache it
        file_hash = calculate_file_hash(file_path)[:10]
        cache_file_hash(file_path, file_hash)
        return file_hash


class D2_CheckpointLoader:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "ckpt_name": (folder_paths.get_filename_list("checkpoints"), ),
            },
            "hidden": {
                "unique_id": "UNIQUE_ID",
                "extra_pnginfo": "EXTRA_PNGINFO",
                "prompt": "PROMPT"}
            }

    RETURN_TYPES = ("MODEL", "CLIP", "VAE", "STRING", "STRING", "STRING")
    RETURN_NAMES = ("model", "clip", "vae", "ckpt_name", "ckpt_hash", "ckpt_fullpath")
    FUNCTION = "load_checkpoint"

    CATEGORY = "D2"

    def load_checkpoint(self, ckpt_name, output_vae=True, output_clip=True, unique_id=None, extra_pnginfo=None, prompt=None):
        ckpt_path = folder_paths.get_full_path("checkpoints", ckpt_name)
        print("fullpath", ckpt_path)
        out = comfy.sd.load_checkpoint_guess_config(ckpt_path, output_vae=True, output_clip=True, embedding_directory=folder_paths.get_folder_paths("embeddings"))
        hash = get_file_hash(ckpt_path)
        ckpt_name = os.path.basename(ckpt_name)
        return out[:3] + (ckpt_name, hash, ckpt_path)
