package ru.itis.vkr.dto;

import lombok.Builder;
import lombok.Getter;
import ru.itis.vkr.model.Player;

@Builder
@Getter
public class PlayerDto {

    private String fio;
    private String url;
    private String position;
    private String team;

    public static PlayerDto from(Player player) {
        return PlayerDto.builder()
                .fio(player.getFio())
                .position(player.getPosition())
                .url(player.getUrl())
                .team(player.getTeam())
                .build();
    }
}
