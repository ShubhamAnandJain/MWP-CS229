# -*- encoding: utf-8 -*-
# @Author: Yihuai Lan
# @Time: 2021/08/29 21:48:54
# @File: transformer_encoder.py


import torch
from torch import nn

from mwptoolkit.module.Layer.transformer_layer import TransformerLayer,GAEncoderLayer,LayerNorm
from mwptoolkit.utils.utils import clones

class TransformerEncoder(nn.Module):
    r"""
    The stacked Transformer encoder layers.
    """
    def __init__(self,
                 embedding_size,
                 ffn_size,
                 num_encoder_layers,
                 num_heads,
                 attn_dropout_ratio=0.0,
                 attn_weight_dropout_ratio=0.0,
                 ffn_dropout_ratio=0.0):
        super(TransformerEncoder, self).__init__()

        self.transformer_layers = nn.ModuleList()
        for _ in range(num_encoder_layers):
            self.transformer_layers.append(
                TransformerLayer(embedding_size, ffn_size, num_heads, attn_dropout_ratio, attn_weight_dropout_ratio,
                                 ffn_dropout_ratio))

    def forward(self, x, kv=None, self_padding_mask=None, output_all_encoded_layers=False):
        r""" Implement the encoding process step by step.

        Args:
            x (torch.Tensor): target sequence embedding, shape: [batch_size, sequence_length, embedding_size].
            kv (torch.Tensor): the cached history latent vector, shape: [batch_size, sequence_length, embedding_size], default: None.
            self_padding_mask (torch.Tensor): padding mask of target sequence, shape: [batch_size, sequence_length], default: None.
            output_all_encoded_layers (Bool): whether to output all the encoder layers, default: ``False``.

        Returns:
            torch.Tensor: output features, shape: [batch_size, sequence_length, ffn_size].
        """
        all_encoded_layers = []
        for idx, layer in enumerate(self.transformer_layers):
            x, _, _ = layer(x, kv, self_padding_mask)
            all_encoded_layers.append(x)
        if output_all_encoded_layers:
            return all_encoded_layers
        return all_encoded_layers[-1]


class GroupATTEncoder(nn.Module):
    """Group attentional encoder, N layers of group attentional encoder layer.
    """

    def __init__(self, layer, N):
        super(GroupATTEncoder, self).__init__()
        self.layers = clones(layer, N)
        self.norm = LayerNorm(layer.size)

    def forward(self, inputs, mask):
        """Pass the input (and mask) through each layer in turn.

        Args:
            inputs (torch.Tensor): input variavle, shape [batch_size, sequence_length, hidden_size].
        
        Returns:
            torch.Tensor: encoded variavle, shape [batch_size, sequence_length, hidden_size].
        """
        for layer in self.layers:
            inputs = layer(inputs, mask)
        return self.norm(inputs)

