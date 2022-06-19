package ru.itis.vkr.dto;

import lombok.Builder;
import lombok.Getter;

@Builder
@Getter
public class SearchPlayersDto {

    String team;
    String position;
}
