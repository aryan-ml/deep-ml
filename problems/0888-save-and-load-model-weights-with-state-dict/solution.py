import io
import torch
import torch.nn as nn

def copy_weights(src: nn.Module, dst: nn.Module) -> nn.Module:
    # TODO: serialize src's state dict into a buffer, rewind, then load it into dst
    
    buffer = io.BytesIO() ## This is like a fake file in RAM or a in memory file 

    state = src.state_dict()

    torch.save(state, buffer)
    buffer.seek(0)

    state = torch.load(buffer)
    dst.load_state_dict(state)

    return dst
